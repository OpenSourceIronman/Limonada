import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { MatDatepickerInputEvent } from '@angular/material';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  events: string[] = [];

  addEvent(type: string, event: MatDatepickerInputEvent<Date>) {
    this.events.push(`${type}: ${event.value}`);
    let selectedDate = event.value;
    const today = new Date();
    const birthDate = new Date(selectedDate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();

    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }

    if (age >= 18) {
      this.isShow = true;
    } else {
      this.isShow = false;
    }
    return this.isShow;
  }

  date = new FormControl(new Date());
  value: Date = new Date();
   getYear : any;
  checkDate: Date;
  form: FormGroup;
  isShow:boolean;
  today = new Date();
  constructor(private fb: FormBuilder , private router:Router ) {
    this.form = this.fb.group({
      format1: new FormControl(new Date()),
      format2: new FormControl(new Date())
    });
  }
  btnClick = function () {
    if ( this.isShow === true ) {
      this.router.navigateByUrl('/second');
    }

};
  // addEvent(type: string, event: MatDatepickerInputEvent<Date>) {
  //   debugger
  //   this.checkDate = event.target.value;
  //   this.getYear = this.checkDate;

  // }
}
