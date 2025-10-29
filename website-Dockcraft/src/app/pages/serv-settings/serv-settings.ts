import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

type Server = {
  username: string;
  players: string;
  ip: string;
  image: string;
  status: 'Running' | 'Stopped';
  uptime: string;
};

@Component({
  selector: 'app-serv-settings',
  imports: [CommonModule],
  templateUrl: './serv-settings.html',
  styleUrls: ['./serv-settings.scss'] 
})
export class ServSettings {
  data: Record<string, Server> = {
    '123': {
      username: 'Jean Dupont',
      players: '12/100',
      ip: 'play.dockcraft.fr:2557',
      image: 'test/image:latest',
      status: 'Running',
      uptime: '03:45:12',
    },
  };

  id = '';

  username = '';
  players = '';
  ip = '';
  image = '';
  status: 'Running' | 'Stopped' = 'Stopped';
  uptime = '';

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe((map) => {
      this.id = map.get('id') ?? '';
      const item = this.data[this.id];

      if (item) {
        this.username = item.username;
        this.players = item.players;
        this.ip = item.ip;
        this.image = item.image;
        this.status = item.status;
        this.uptime = item.uptime;
      } else {
        // id inconnu : gère un fallback ou une redirection
        // ex: this.router.navigate(['/404']);
      }
    });
  }
}
