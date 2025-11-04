import { Component, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface ModLoader {
  value: string;
  viewValue: string;
}

interface Version {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-create',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './create.html',
  styleUrls: ['./create.scss']
})
export class Create {
  worldName: string = '';
  maxPlayers: number = 20;
  selectedVersion: string = '';
  adminList: string[] = ['Killer2Feu', 'Xx_DockerWSL06_xX', 'BigardiDu24'];
  
  isModLoaderOpen: boolean = false;
  isVersionOpen: boolean = false;

  selectedModLoader: string = '';
  
  modsLoader: ModLoader[] = [
    { value: 'forge', viewValue: 'Forge' },
    { value: 'fabric', viewValue: 'Fabric' },
    { value: 'paper', viewValue: 'Paper' },
    { value: 'neoforge', viewValue: 'NeoForge' },
    { value: 'vanilla', viewValue: 'Vanilla' }
  ];

    versions: Version[] = [
    { value: '1.12.1', viewValue: '1.21.1' }
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

  toggleModLoaderDropdown(): void {
    this.isModLoaderOpen = !this.isModLoaderOpen;
  }

  selectModLoader(loader: string): void {
    this.selectedModLoader = loader;
    this.isModLoaderOpen = false;
  }


  toggleVersionDropdown(): void {
    this.isVersionOpen = !this.isVersionOpen;
  }

  selectVersion(version: string): void {
    this.selectedVersion = version;
    this.isVersionOpen = false;
  }

  @HostListener('document:click', ['$event'])
  clickOutside(event: Event): void {
    const target = event.target as HTMLElement;
    if (!target.closest('.mod-loader-dropdown')) {
      this.isModLoaderOpen = false;
    }

        if (!target.closest('.version-dropdown')) {
      this.isVersionOpen = false;
    }
  }
}