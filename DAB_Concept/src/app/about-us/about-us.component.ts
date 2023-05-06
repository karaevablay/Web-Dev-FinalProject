import { Component, OnInit } from '@angular/core';
import {Member, Project} from "../models";
import {DataService} from "../data.service";

@Component({
  selector: 'app-about-us',
  templateUrl: './about-us.component.html',
  styleUrls: ['./about-us.component.css']
})
export class AboutUsComponent implements OnInit {

  membersInfo: Member[] = [];
  projects: Project[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.getMembersInfo();
    this.getProjects();
  }

  scrollUp() {
    window.scroll({
      top: 0,
      left: 0,
      behavior: 'smooth',
    });
  }

  getMembersInfo() {
    this.dataService.getMembersInfo().subscribe(data => {
      this.membersInfo = data;
    });
  }

  getProjects() {
    this.dataService.getProjects().subscribe(data => {
      this.projects = data;
    });
  }

  redirect(url: string) {
    window.location.href = url;
  }
}
