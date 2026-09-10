export interface Client {
  id: number;
  client_name: string;
  email: string;
  phone: string | null;
  company: string | null;
  city: string | null;
  status: string;
}