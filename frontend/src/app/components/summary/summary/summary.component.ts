import { Component } from '@angular/core';

import { ApiService } from '../../../services/api.service';

import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { CommonModule } from '@angular/common';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-summary',
  standalone: true,
  imports: [
  CommonModule,
  MatButtonModule,
  MatCardModule,
  MatProgressSpinnerModule
  ],
  templateUrl: './summary.component.html',
  styleUrl: './summary.component.css'
})
export class SummaryComponent {

  summary = '';

  loading = false;

  constructor(
    private apiService: ApiService
  ) {}

  generateSummary() {

    this.loading = true;

    this.apiService.getSummary().subscribe({

      next: (response) => {

        this.summary = response.summary;

        this.loading = false;

      },

      error: () => {

        this.summary = 'Unable to generate summary.';

        this.loading = false;

      }

    });

  }

}