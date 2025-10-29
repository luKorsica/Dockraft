import { Component } from '@angular/core';
import { ServerCard } from '../../server-card/server-card';

@Component({
  selector: 'app-home',
  imports: [ServerCard],
  templateUrl: './home.html',
  styleUrl: './home.scss',
  imports: [SwitchComponent]
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
