import { Component, OnInit } from '@angular/core';
import {MemberInfo} from "../models";
import {DataService} from "../data.service";

@Component({
  selector: 'app-portfolio-details',
  templateUrl: './portfolio-details.component.html',
  styleUrls: ['./portfolio-details.component.css']
})
export class PortfolioDetailsComponent implements OnInit {

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
