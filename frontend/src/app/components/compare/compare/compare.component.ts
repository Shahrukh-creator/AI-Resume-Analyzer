import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { ApiService } from '../../../services/api.service';

import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-compare',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatCardModule,
    MatButtonModule,
    MatInputModule,
    MatFormFieldModule,
    MatProgressSpinnerModule
  ],
  templateUrl: './compare.component.html',
  styleUrl: './compare.component.css'
})
export class CompareComponent {

  jobDescription = '';

  comparison = '';

  loading = false;

  constructor(
    private apiService: ApiService
  ) {}

  compareResume() {

    if (!this.jobDescription.trim()) {

      this.comparison = 'Please enter a Job Description.';

      return;

    }

    this.loading = true;

    this.apiService.compareResume(this.jobDescription)
      .subscribe({

        next: (response) => {

          this.comparison = response.comparison;

          this.loading = false;

        },

        error: () => {

          this.comparison = 'Comparison failed.';

          this.loading = false;

        }

      });

  }

}