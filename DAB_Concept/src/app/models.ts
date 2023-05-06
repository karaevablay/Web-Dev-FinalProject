export interface AuthToken {
    token: string;
}

export interface Member {
    id: number;
    first_name: string;
    last_name: string;
    photo: string;
    brief_info: string;
}

export interface MemberInfo {
    member: Member;
    email: string;
    about: string;
    education: string;
    skills: string;
    hobbies: string;
    github: string;
    tg: string;
}

export interface Blog {
    id: number;
    member: Member;
    title: string;
    creation_date: Date;
    content: string;
}

export interface Project {
    id: number;
    photo: string;
    title: string;
    brief_info: string;
    link: string;
}
