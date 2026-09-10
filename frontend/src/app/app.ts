import { CommonModule } from '@angular/common';
import { Component, computed, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Client } from './models/client';
import { ClientService } from './services/client.service';
import { ClientStatus } from './constants/app.constants';

@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class AppComponent {
  private readonly clientService = inject(ClientService);

  readonly clients = signal<Client[]>([]);
  readonly loading = signal(true);
  readonly error = signal('');
  readonly searchTerm = signal('');
  readonly clientId = signal('');
  readonly searchedClient = signal<Client | null>(null);
  readonly lookupLoading = signal(false);
  readonly lookupError = signal('');

  readonly filteredClients = computed(() => {
    const searchTerm = this.searchTerm().trim().toLowerCase();

    return this.clients().filter((client) =>
      [client.client_name, client.email, client.phone].some((value) =>
        value?.toLowerCase().includes(searchTerm),
      ),
    );
  });

  constructor() {
    this.loadClients();
  }

  get activeClientCount(): number {
    return this.clients().filter((client) => client.status === ClientStatus.Active).length;
  }

  get pendingClientCount(): number {
    return this.clients().filter((client) => client.status === ClientStatus.Pending).length;
  }

  updateClientId(clientId: number | string | null): void {
    this.clientId.set(clientId?.toString() ?? '');
  }

  handleClientLookup(): void {
    const clientId = this.clientId().trim();

    if (!clientId) {
      this.lookupError.set('Enter a client ID to search.');
      this.searchedClient.set(null);
      return;
    }

    this.lookupLoading.set(true);
    this.lookupError.set('');
    this.searchedClient.set(null);

    this.clientService.getClient(clientId).subscribe({
      next: (client) => this.searchedClient.set(client),
      error: (error: { status?: number }) => {
        this.lookupError.set(
          error.status === 404 ? 'No client found with that ID.' : 'Unable to look up the client.',
        );
      },
      complete: () => this.lookupLoading.set(false),
    });
  }

  private loadClients(): void {
    this.clientService.getClients().subscribe({
      next: (clients) => this.clients.set(clients),
      error: () => this.error.set('Unable to load clients'),
      complete: () => this.loading.set(false),
    });
  }
}