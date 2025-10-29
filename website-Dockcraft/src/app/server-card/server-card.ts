import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-server-card',
  imports: [CommonModule],
  templateUrl: './server-card.html',
  styleUrl: './server-card.scss'
})
export class ServerCard {
  @Input() name!: string;
  @Input() status!: "Running" | "Stopped";
  @Input() image!: string;
  @Input() uptime!: string;
  @Input() ip!: string;
  @Input() players!: string;
}
