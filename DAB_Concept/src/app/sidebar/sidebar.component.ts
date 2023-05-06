import { Component, OnInit } from '@angular/core';
import {DataService} from "../data.service";
import {MemberInfo} from "../models";

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {

  memberInfo: MemberInfo = {
    "member": {
      "id": 0,
      "first_name": "",
      "last_name": "",
      "photo": "",
      "brief_info": ""
    },
    "email": "",
    "about": "",
    "education": "",
    "skills": "",
    "hobbies": "",
    "github": "",
    "tg": ""
  };

  member: string = window.location.pathname.replace(/.*\//, '');
  memberId: number = (this.member == 'adil') ? 1 : (this.member == 'beka') ? 2 : 3;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.getMemberInfo();
  }

  getMemberInfo() {
    this.dataService.getMemberInfo(this.memberId).subscribe(data => {
      console.log(data);
      this.memberInfo = data;
    });
  }

}
