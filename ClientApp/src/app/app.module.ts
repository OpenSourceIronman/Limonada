import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { NavMenuComponent } from './nav-menu/nav-menu.component';
import { HomeComponent } from './home/home.component';
import { CounterComponent } from './counter/counter.component';
import { FetchDataComponent } from './fetch-data/fetch-data.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDatepickerModule, MatInputModule, MatNativeDateModule, MatFormFieldModule, MatDividerModule} from '@angular/material';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { SecondComponentComponent } from './second-component/second-component.component';
import { MatRippleModule } from '@angular/material/core';

import { KaypadComponent } from './kaypad/kaypad.component';
import { MatDialogModule } from '@angular/material/dialog';

@NgModule({
  entryComponents: [
    KaypadComponent
  ],
  declarations: [
    AppComponent,
    NavMenuComponent,
    HomeComponent,
    SecondComponentComponent,
    CounterComponent,
    FetchDataComponent,
    KaypadComponent
  ],
  imports: [
    BrowserModule.withServerTransition({appId: 'ng-cli-universal'}),
    HttpClientModule, 
    FormsModule,
    ReactiveFormsModule, 
    MatCardModule, 
    MatButtonModule,
    MatDatepickerModule, 
    MatFormFieldModule, 
    MatRippleModule,
    MatInputModule, 
    MatNativeDateModule,
    MatIconModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent, pathMatch: 'full'},
      {path: 'counter', component: CounterComponent},
      {path: 'second', component: SecondComponentComponent},
    ]),
    BrowserAnimationsModule, 
    MatDividerModule,
    MatDialogModule,
    MatIconModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
