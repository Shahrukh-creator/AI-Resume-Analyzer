import { Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard/dashboard.component';
import { UploadComponent } from './components/upload/upload/upload.component';
import { SummaryComponent } from './components/summary/summary/summary.component';
import { AtsComponent } from './components/ats/ats/ats.component';
import { CompareComponent } from './components/compare/compare/compare.component';
import { InterviewComponent } from './components/interview/interview/interview.component';



export const routes: Routes = [

  {
    path: '',
    component: DashboardComponent
  },

  {
    path: 'upload',
    component: UploadComponent
  },

  {
    path: 'summary',
    component: SummaryComponent
  },

  {
    path: 'ats',
    component: AtsComponent
  },

  {
    path: 'compare',
    component: CompareComponent
  },

  {
    path: 'interview',
    component: InterviewComponent
  },

  {
    path: '**',
    redirectTo: ''
  }

];