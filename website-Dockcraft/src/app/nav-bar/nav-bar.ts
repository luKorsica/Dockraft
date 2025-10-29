import { Component } from '@angular/core';
import { Router, NavigationEnd, RouterModule } from '@angular/router';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-nav-bar',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './nav-bar.html',
  styleUrls: ['./nav-bar.scss'] 
})
export class NavBar {
  public current_route: string = '';

  constructor(private router: Router) {}

  ngOnInit() {
    this.current_route = this.router.url.split('/')[1] || '';

    this.router.events
      .pipe(filter(event => event instanceof NavigationEnd))
      .subscribe((event: any) => {
        this.current_route = event.url.split('/')[1] || '';
      });
  }
}
