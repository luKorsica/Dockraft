import { Component } from '@angular/core';
import { ServerCard } from '../../server-card/server-card';
import { SwitchComponent } from '../../switch-button/switch-button';

@Component({
  selector: 'app-home',
  imports: [ServerCard, SwitchComponent],
  templateUrl: './home.html',
  styleUrl: './home.scss'
})
export class Home {
username = 'Jean Dupont'; 
players = '12/100';
ip = 'play.dockcraft.fr:2557';
image = 'test/image:lastest';
status: "Running" | "Stopped" = "Running";
status2: "Running" | "Stopped" = "Stopped";
uptime = '03:45:12';
}
