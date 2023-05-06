import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-mainbar',
  templateUrl: './mainbar.component.html',
  styleUrls: ['./mainbar.component.css']
})
export class MainbarComponent implements OnInit {

  flag: string = "portfolio";

  constructor() { }

  ngOnInit(): void {
  }

  show_portfolio() {
    this.flag = "portfolio";
  }

  show_blogs() {
    this.flag = "blogs";
  }

  show_admin_panel() {
    this.flag = "admin";
  }

}
