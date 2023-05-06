import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
  logged = false;
  username = '';
  password = '';

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if(token) {
      this.logged = true;
    }
  }

  login() {
    this.dataService.login(this.username, this.password).subscribe((data) => {

      localStorage.setItem('token', data.token);

      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }

  logout() {
    this.logged = false;
    localStorage.removeItem('token');
  }

}
