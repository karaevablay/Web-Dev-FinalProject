import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PortAdilComponent } from './port-adil.component';

describe('PortAdilComponent', () => {
  let component: PortAdilComponent;
  let fixture: ComponentFixture<PortAdilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PortAdilComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PortAdilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
