import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Login } from './pages/login/login';
import { ServSettings } from './pages/serv-settings/serv-settings';


export const routes: Routes = [
    {path:"", component:Home},
    {path:"login", component:Login},
    {path:"serv-settings/:id", component:ServSettings}

];
