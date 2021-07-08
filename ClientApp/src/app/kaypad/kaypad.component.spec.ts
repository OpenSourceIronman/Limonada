import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KaypadComponent } from './kaypad.component';

describe('KaypadComponent', () => {
  let component: KaypadComponent;
  let fixture: ComponentFixture<KaypadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KaypadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KaypadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
