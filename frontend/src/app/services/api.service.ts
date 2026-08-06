import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(
    private http: HttpClient
  ) {}

  uploadResume(file: File): Observable<any> {

    const formData = new FormData();

    formData.append('file', file);

    return this.http.post(
      `${this.baseUrl}/upload`,
      formData
    );
  }

  getSummary(): Observable<any> {

    return this.http.get(
      `${this.baseUrl}/summary`
    );
  }

  getATS(): Observable<any> {

    return this.http.get(
      `${this.baseUrl}/ats`
    );
  }

  compareResume(jobDescription: string): Observable<any> {

    return this.http.post(
      `${this.baseUrl}/compare`,
      {
        job_description: jobDescription
      }
    );
  }

  generateInterviewQuestions(jobDescription: string): Observable<any> {

    return this.http.post(
      `${this.baseUrl}/interview`,
      {
        job_description: jobDescription
      }
    );
  }

}