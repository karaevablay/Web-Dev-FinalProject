import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PortDanComponent } from './port-dan.component';

describe('PortDanComponent', () => {
  let component: PortDanComponent;
  let fixture: ComponentFixture<PortDanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PortDanComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PortDanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
