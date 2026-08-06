import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ApiService } from '../../../services/api.service';

import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-ats',
  standalone: true,
  imports: [
    CommonModule,
    MatButtonModule,
    MatCardModule,
    MatProgressSpinnerModule
  ],
  templateUrl: './ats.component.html',
  styleUrl: './ats.component.css'
})
export class AtsComponent {

  analysis = '';

  loading = false;

  constructor(
    private apiService: ApiService
  ) {}

  analyzeResume() {

    this.loading = true;

    this.apiService.getATS().subscribe({

      next: (response) => {

        this.analysis = response.analysis;

        this.loading = false;

      },

      error: () => {

        this.analysis = 'Unable to analyze resume.';

        this.loading = false;

      }

    });

  }

}
