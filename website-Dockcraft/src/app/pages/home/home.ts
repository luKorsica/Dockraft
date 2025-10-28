import { Component } from '@angular/core';
import { SwitchComponent } from '../../switch-button/switch-button';

@Component({
  selector: 'app-home',
  standalone: true,
  templateUrl: './home.html',
  styleUrl: './home.scss',
  imports: [SwitchComponent]
})
export class Home {
  isOn = false;
}
