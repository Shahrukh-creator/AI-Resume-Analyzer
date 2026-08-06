import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import  { ApiService } from '../../../services/api.service';

import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-interview',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    MatProgressSpinnerModule
  ],
  templateUrl: './interview.component.html',
  styleUrl: './interview.component.css'
})
export class InterviewComponent {

  jobDescription = '';

  questions = '';

  loading = false;

  constructor(
    private apiService: ApiService
  ) {}

  generateQuestions() {

    if (!this.jobDescription.trim()) {

      this.questions = 'Please enter a Job Description.';

      return;

    }

    this.loading = true;

    this.apiService
      .generateInterviewQuestions(this.jobDescription)
      .subscribe({

        next: (response) => {

          this.questions = response.questions;

          this.loading = false;

        },

        error: () => {

          this.questions = 'Unable to generate interview questions.';

          this.loading = false;

        }

      });

  }

}