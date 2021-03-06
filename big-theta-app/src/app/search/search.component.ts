import { Component, OnInit } from '@angular/core';
import { CompleterService, CompleterData, CompleterItem } from 'ng2-completer';

import { AuthService } from '../services/auth.service';
import { GraphSearchService } from 'app/services/graph-search.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  protected equationStr: string;
  protected dataService: CompleterData;
  searchQuote = "Enter a topic";
 
  constructor(private completerService: CompleterService, private _authService:AuthService, private _graphSearchService: GraphSearchService) {
    this.dataService = this.completerService.remote('https://r3psss9s0a.execute-api.us-east-1.amazonaws.com/bigtheta/subject/search/', this.equationStr, 'title').searchFields('title');
  }
  
  equSelected(selected: CompleterItem) {
    if (selected) {
      this._graphSearchService.newSearch(selected.originalObject.id);
      this._graphSearchService.newEquationSubject({ id: selected.originalObject.id, title: selected.originalObject.title, url: selected.originalObject.url });
    }
  }

  ngOnInit() {
  }

}
