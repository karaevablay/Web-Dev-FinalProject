import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {AuthToken, MemberInfo, Project, Member} from './models';

import { Blog } from './models';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }

  getBlogs(): Observable<Blog[]> {
    return this.http.get<Blog[]>(`${this.BASE_URL}/api/blogs/`);
  }

  getMemberInfo(id: number): Observable<MemberInfo> {
    return this.http.get<MemberInfo>(`${this.BASE_URL}/api/members/${id}/`);
  }

  getMembersInfo(): Observable<Member[]> {
    return this.http.get<Member[]>(`${this.BASE_URL}/api/members/`);
  }

  getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>(`${this.BASE_URL}/api/projects/`);
  }

}
