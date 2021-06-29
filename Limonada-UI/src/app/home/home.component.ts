import {Component, OnInit} from '@angular/core';
import {FormControl, ValidationErrors} from "@angular/forms";
import {NgxAgeValidator} from "ngx-age-validator";
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatError} from "@angular/material/form-field";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {


  ageFormControl = new FormControl();

  ngOnInit(): void {
    this.ageFormControl = new FormControl(null, [NgxAgeValidator(18, 40)])

    this.ageFormControl.valueChanges.subscribe(() => {

      const controlErrors: ValidationErrors | null = this.ageFormControl.errors;
      if (controlErrors != null) {
        Object.keys(controlErrors).forEach(keyError => {
          console.log(' keyError: ' + keyError + ', err value: ', controlErrors[keyError]);
        });
      }

    })
  }

}
