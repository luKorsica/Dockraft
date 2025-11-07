import { Injectable, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { Image } from './image.interface';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private http = inject(HttpClient);
  private users = signal<Image[]>([])
  readonly url = 'https://jsonplaceholder.typicode.com/users';

  getUsers(): Observable<Image[]> {
    return this.http.get<Image[]>(this.url).pipe(
      tap(users => this.users.set(users))
    );
  }
}