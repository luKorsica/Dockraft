import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-create',
  standalone: true,
  imports: [CommonModule, FormsModule], // Assurez-vous que FormsModule est ici
  templateUrl: './create.html',
  styleUrls: ['./create.scss']
})
export class Create {
  worldName: string = '';
  maxPlayers: number = 20;
  selectedVersion: string = 'Forge 1.21';
  
  adminList: string[] = ['Slimed', 'Killer2Feu', 'Xx_DockerWSL06_xX', 'BigardiDu24'];
  
  modsLoader: string[] = [
    "Paper",
    "Forge",
    "Fabric"
];

  addAdmin(): void {
    const newAdmin = prompt('Enter admin username:');
    if (newAdmin && newAdmin.trim()) {
      this.adminList.push(newAdmin.trim());
    }
  }

  removeAdmin(index: number): void {
    this.adminList.splice(index, 1);
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      console.log('File selected:', input.files[0].name);
    }
  }
}