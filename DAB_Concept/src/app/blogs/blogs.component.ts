import { Component, OnInit } from '@angular/core';
import { Blog } from '../models';
import { DataService } from '../data.service';

@Component({
  selector: 'app-blogs',
  templateUrl: './blogs.component.html',
  styleUrls: ['./blogs.component.css']
})
export class BlogsComponent implements OnInit {

  blogs: Blog[] = [];
  member: string = window.location.pathname.replace(/.*\//, '');
  memberFirstName = (this.member == 'adil') ? 'Adil' : (this.member == 'beka') ? 'Bekzat' : 'Daniyar';

  // for retrieving specific blog from list
  specificBlog: Blog = this.blogs[0];
  // show list of blogs or blog
  showSpecificBlog: boolean = false;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.getBlogs();
  }

  getBlogs() {
    this.dataService.getBlogs().subscribe((data) => {
      this.blogs = data;
    });
  }

  showBlog(blog: Blog) {
    this.specificBlog = blog;
    this.showSpecificBlog = true;
  }

  hideBlog() {
    this.showSpecificBlog = false;
  }

}
