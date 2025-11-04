export interface Server {
    id: string;
    name: string;
    version: string;
    modLoader: string;
    maxPlayers: number;
    admins: string[];
}