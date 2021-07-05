import { Component } from '@angular/core';
import { AbstractControl, FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators } from '@angular/forms';
import {  ErrorStateMatcher, MatDatepickerInputEvent } from '@angular/material';
import { Router } from '@angular/router';

export function AgeValidator(control: AbstractControl): { [key: string]: boolean } | null {
  const today = new Date();
  const birthDate = new Date(control.value);
  let age = today.getFullYear() - birthDate.getFullYear();
  const m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }

  debugger

  if (age < 21) {
    return { 'age': true };
  }
  return null;
}
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  events: string[] = [];
  isShow:boolean;
  today = new Date();

  // addEvent(type: string, event: MatDatepickerInputEvent<Date>) {
  //   debugger
  //   this.events.push(`${type}: ${event.value}`);
  //   let selectedDate = event.value;
  //   const today = new Date();
  //   const birthDate = new Date(selectedDate);
  //   let age = today.getFullYear() - birthDate.getFullYear();
  //   const m = today.getMonth() - birthDate.getMonth();
  //   debugger
  //   if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
  //     age--;
  //   }

  //   if (age >= 18) {
  //     this.isShow = true;
  //   }
  //   else {
  //     return  this.isShow = false;
  //   }
  //   return this.isShow;
  // }

  constructor(private _formBuilder: FormBuilder , private router:Router ) {
  }
  validatorForm = this._formBuilder.group({
    dob:['', [Validators.required, AgeValidator]]
    // name:['',Validators.required]
  })
  get dob() {
    return this.validatorForm.get('dob');
  }
  public hasError = (controlName: string, errorName: string) => {
    return this.validatorForm.controls[controlName].hasError(errorName);
  }
  btnClick = function () {
    debugger
    if (this.validatorForm.valid) {
      console.log(this.validatorForm.value)
      this.router.navigateByUrl('/second');
    }

};
}
