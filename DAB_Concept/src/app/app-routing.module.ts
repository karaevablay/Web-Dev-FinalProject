import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from './auth/auth.component';
import { HomePageComponent } from './home-page/home-page.component';
import { PortAdilComponent } from './port-adil/port-adil.component';
import { PortBekaComponent } from './port-beka/port-beka.component';
import { PortDanComponent } from './port-dan/port-dan.component';

const routes: Routes = [
  // { path: '', pathMatch: 'full', redirectTo: '/home'},
  { path: '', component: HomePageComponent},
  { path: 'home', component: HomePageComponent},

  { path: 'adil', component: PortAdilComponent},

  { path: 'beka', component: PortBekaComponent},

  { path: 'dan', component: PortDanComponent},

  { path: 'auth', component: AuthComponent},

  { path: '**', component: HomePageComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
