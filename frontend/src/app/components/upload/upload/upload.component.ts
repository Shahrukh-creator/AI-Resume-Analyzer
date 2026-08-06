import { Component } from '@angular/core';

import { ApiService } from '../../../services/api.service';

import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [
    MatButtonModule,
    CommonModule,
    MatCardModule,
    MatProgressSpinnerModule
  ],
  templateUrl: './upload.component.html',
  styleUrl: './upload.component.css'
})
export class UploadComponent {

  selectedFile!: File;

  message = '';

  uploading = false;

  constructor(
    private apiService: ApiService
  ) {}

  onFileSelected(event: Event) {

    const input = event.target as HTMLInputElement;

    if (input.files?.length) {

      const file = input.files[0];
    
      if (file.type !== 'application/pdf') {
    
        this.message = 'Please select a PDF file.';
        return;
    
      }
    
      this.selectedFile = file;
      this.message = '';
    
    }

  }

  uploadResume() {

    if (!this.selectedFile) {

      this.message = 'Please select a PDF.';

      return;

    }

    this.uploading = true;

    this.apiService
      .uploadResume(this.selectedFile)
      .subscribe({

        next: (response) => {

          this.message = response.message;

          this.uploading = false;

        },

        error: () => {

          this.message = 'Upload failed.';

          this.uploading = false;

        }

      });

  }

}