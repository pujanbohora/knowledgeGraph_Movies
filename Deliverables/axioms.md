**Actor**<br>
     ![actor](../schema-diagrams/Actor/actor.jpg)

1.  `ActorRole SubClass Of AgentRole` <br> 
     Actor roles are a type of agent role. <br> 

2.  `providesActorRole exactly 1 ActorRole` <br> 
     Each movie provides exactly one actor role. <br> 
 
3.  `hasTemporalExtent exactly 1 TemporalExtent` <br> 
     Each actor role has exactly one temporal extent. <br> 

4.  `LeadRole SubClass Of ActorRole SupportingRole SubClass Of ActorRole` <br> 
     Lead and supporting roles are specific types of actor roles <br> 

5.  `hasScreenTime exactly 1 xsd:int` <br> 
     Both lead and supporting roles have exactly one screen time attribute of type integer. <br> 

6.  `hasFanBase exactly 1 xsd:String` <br> 
     Each lead role has exactly one fan base attribute of type string. <br> 

7. `hasBackStory exactly 1 xsd:String` <br> 
    Each supporting role has exactly one backstory attribute of type string. <br> 

8.  `performsActorRole Domain Agent` <br> 
     Actor roles are defined within the context of agents. <br> 

9.  `providesActorRole Domain Movie` <br> 
     The Movie entity has a mandatory relationship with ActorRole. <br> 



**Budget**<br>
    ![budget](../schema-diagrams/Budget/budget.jpg)

1. `Budget hasQuantityValue exactly 1 QuantityValue` <br>
    Every Budget has exactly one QuantityValue<br>
    
2. `QuantityValue hasQuantityKind exactly 1 QuantityKind`<br>
    Every QuantityValue has exactly one QuantityKind<br>

3.  `QuantityValue hasUnit exactly 1 Unit`<br>
     Every QuantityValue has exactly one Unit.<br> 
    
4.  `QuantityValue hasNumericValue exactly 1 xsd:double`<br>
     Every QuantityValue has exactly one numeric value of type xsd:double. <br>

**Country**<br>
    ![country](../schema-diagrams/Country/country.jpg)

1.  `ProductionCompany basedIn min 1 Place`<br>

     The Production Company is based in at least one Place. <br>


2.  `Movie hasFilmingLocation min 1 Place`<br>
     The Movie has at least one filming location. <br>

3.  `City hasName exactly 1 xsd:String`<br>
     The City has exactly one name, represented as String. <br>

4.  `Person isACitizenOf min 1 Country`<br>
     The person is a citizen of at least one country.<br>

5.  `Country hasCity min 1 City`<br>
     The Country has at least one city.<br>

**Director**<br>
    ![director](../schema-diagrams/Director/Director.jpg)

1.  `Movie providesDirectorRole min 1 DirectorRole`<br>
     The Movie provides at least one DirectorRole.<br>

2.  `Agent performsDirectorRole min 1 DirectorRole`<br>
     The Agent performs at least one DirectorRole.<br>

3.  `DirectorRole hasTemporalExtent exactly 1 TemporalExtent`<br>
     The DirectorRole has exactly one TemporalExtent.<br>

4.   `MainDirector hasKeyDecision exactly 1 xsd:string`<br>
      The MainDirector has exactly one directorial vision, represented as string.<br> 

5.    `MainDirector has DirectorialVision exactly 1 xsd:string`<br>
       MainDirector has exactly one directorial vision, represented as string. <br>

6.    `TechnicalDirector hasTechnicalChallenge min 1 xsd:string`<br>
      The TechnicalDirector has at least one technical challenge, represented as string.<br>

7.    `TechnicalDirector hasTechnologyUsed min 1 xsd:string`<br>
       The TechnicalDirector uses at least one type of technology, represented as string. <br>

**Genere**<br>

1.  `Genere hasTargetAudience exactly 1 xsd:string`<br>
     The Genere has exactly one target audience, represented as string. <br>
        ![genere](../schema-diagrams/Genere/Genere.jpg)

1.  `Genere hasTargetAudience exactly 1 xsd:string`<br>
     The Genere has exactly one target audience, represented as string.<br> 


2.  `Genere hasOrigin exactly 1 xsd:string`<br>
     The Genere has exactly one origin, represented as string. <br>
     
3.  `Comedy subClassOf Genere`<br>
     `Action subClassOf Genere`<br>
     `Horror subClassOf Genere`<br>
     Comedy,Action and Horror are subclasses of Genere.<br>
     
4.  `DarkComedy subClassOf Comedy`<br>
    `Staire subClassOf Comedy`<br>
    DarkComedy and Staire are subclass of Comedy<br>

5.  `MartialArts subClassOf Action`<br>
    `Superhero subClassof Action`<br>
     MartialArts and SuperHero are subclasses of Action.<br>

6.  `MonsterHorror subClassOf Horror`<br>
     MonsterHorror is a subClass of Horror. <br>

**GrossEarning**<br>
    ![grossEarning](../schema-diagrams/GrossEarning/grossEarning.jpg)

1.  `GrossEarnings hasEarningValue exactly 1 EarningValue`<br>
    The GrossEarnings has exactly one EarningValue. <br>

2.  `EarningsValue hasNumericValue exactly 1 xsd:int`<br>
     The EarningValue has exactly one numeric value, represented as integer. <br>

3.  `EarningValue hasCurrency exactly 1 currency`<br>
     The EarningValue has exactly one currency. <br>

4.  `GrossEarnings hasEarningsType exactly 1 EarningsType`<br>
     The GrossEarnings has exactly one type of earnings.<br>

**MovieRating**<br>
    ![grossEarning](../schema-diagrams/MovieRating/movieRating.png)

1.  `MovieRatingObservation hasSimpleResult exactly 1 rdfs:NumericUserRatingValue`<br>
    The MovieRatingObservation has exactly one simple result, represented as a numeric user rating value.<br>

2. `MovieRatingObservation observedProperty exactly 1 Rating`<br>
    The MovieRatingObservation observes exactly one property, which is the Rating.<br>

3. `MovieRatingObservation hasResult exactly 1 RatingValue`  <br>
    The MovieRatingObservation has exactly one result, represented by a RatingValue.<br>

4. `MovieRatingObservation hasObservedMovie exactly 1 Movie`<br>
    The MovieRatingObservation is associated with exactly one observed Movie.<br>

5. `MovieRatingObservation hasPhenomenonTime exactly 1 RatingDate`  <br> 

    The MovieRatingObservation has exactly one phenomenon time, represented by the RatingDate.<br>

6. `MovieRatingObservation hasResultTime exactly 1 RatingDate`<br>
    The MovieRatingObservation has exactly one result time, also represented by the RatingDate.<br>

7.  `Platform subClassOf MovieRatingObservation`<br>
    The Platform is a subclass of MovieRatingObservation, indicating that MovieRatingObservation can be further refined by Platform.<br>

**ProducationCompany**<br>
    ![grossEarning](../schema-diagrams/ProductionCompany/ProductionCompanies.jpg)

1.  `Movie providesProductionRole min 1 ProductionRole`<br>
     The Movie provides at least one ProductionRole.<br>

2. `Agent performsAgentRole exactly 1 ProductionRole`<br>
    The Agent performs exactly one ProductionRole.<br>


3. `ProductionRole hasTemporalExtent exactly 1 ProductionPeriod` <br> 
    The ProductionRole has exactly one temporal extent, represented by the ProductionPeriod.<br>

4. `ExecutiveProducer hasFinancialContribution exactly 1 xsd:int`<br>
    The ExecutiveProducer has exactly one financial contribution, represented as an integer.<br>

5. `ExecutiveProducer hasCreativeControl exactly 1 xsd:string`   <br>
    The ExecutiveProducer has exactly one creative control specification, represented as a string.<br>

6.  `ExecutiveProducer hasContractTerms exactly 1 xsd:int`<br>
    The ExecutiveProducer has exactly one contract terms specification, represented as an integer.<br>

7. `Distribution hasRevenueSharePercentage exactly 1 xsd:string`<br>
    The Distribution has exactly one revenue share percentage, represented as a string.<br>

8. `Distribution hasReleasePlatforms min 1 xsd:string`  <br>
    The Distribution has at least one release platform, represented as a string.<br>

9. `Distribution hasDistributionRegion exactly 1 xsd:string`<br>
    The Distribution has exactly one distribution region, represented as a string.<br>


**InflationRate**<br>
    ![InflationRate](../schema-diagrams/InflationRate/inflationRate.jpg)

1.  `InflationObservation contains exactly 1 InflationTimeExtent`<br>
    The InflationObservation contains exactly one InflationTimeExtent.<br>

2. `ObservationPeriod hasDuration exactly 1 xsd:int`<br>
    The ObservationPeriod has exactly one duration, represented as an integer.<br>

3. `ObservationPeriod startsFrom exactly 1 ReleaseDate`  <br>
    The ObservationPeriod has exactly one start date, represented by ReleaseDate.<br>

4. `ObservationPeriod endsAt exactly 1 ReleaseDate`<br>
    The ObservationPeriod has exactly one end date, represented by ReleaseDate.<br>

5. `InflationTimeExtent hasValue exactly 1 InflationRateValue`   <br>
    The InflationTimeExtent has exactly one inflation rate value.<br>

6.  `InflationRateValue hasPercentage exactly 1 xsd:double`<br>
    The InflationRateValue has exactly one percentage value, represented as a double.<br>

7. `ReleaseDate hasReferenceSystem exactly 1 CurrencyReferenceSystem`<br>
    The ReleaseDate has exactly one reference system, represented by CurrencyReferenceSystem.<br>

**UserRating**<br>
    ![grossEarning](../schema-diagrams/UserRating/userRatings.jpg)

1.  `UserRatingObservation hasSimpleResult exactly 1 rdfs:NumericRatingValue`<br>
    The UserRatingObservation has exactly one simple result, represented by a NumericRatingValue.<br>

2. `UserRatingObservation observedProperty exactly 1 RatingType`<br>
    The UserRatingObservation observes exactly one property, which is a RatingType.<br>

3. `UserRatingObservation hasResult exactly 1 RatingValue`  <br>
    The UserRatingObservation has exactly one result, represented by a RatingValue.<br>

4. `UserRatingObservation hasObservedMovie exactly 1 Movie`<br>
    The UserRatingObservation is associated with exactly one observed Movie.<br>

5. `UserRatingObservation hasResultTime exactly 1 RatingDate`   <br>
    The UserRatingObservation has exactly one result time, represented by a RatingDate.<br>

6.  `Platform hasAPlatformName exactly 1 xsd:string`<br>
   The Platform has exactly one name, represented as a string.<br>

7. `RatingType hasADescription exactly 1 xsd:string`<br>
    The RatingType has exactly one description, represented as a string.<br>

7. `RatingType maxScale exactly 1 xsd:int`<br>
    The RatingType has exactly one maximum scale value, represented as an integer.<br>


**Vote**<br>
    ![grossEarning](../schema-diagrams/Vote/vote.jpg)

1.  `VoteObservation hasSimpleResult exactly 1 rdfs:NumericVoteValue`<br>
    The VoteObservation has exactly one simple result, represented by a NumericVoteValue.<br>

2. `VoteObservation observedProperty exactly 1 VoteType`<br>
    The VoteObservation observes exactly one property, which is a VoteType.<br>

3. `VoteObservation hasResult exactly 1 VoteCount`  <br>
    The VoteObservation has exactly one result, represented by a VoteCount.<br>

4. `VoteObservation hasFeatureOfInterest exactly 1 Movie`<br>
    The VoteObservation has exactly one feature of interest, which is a Movie.<br>

5. `VoteObservation hasPhenomenonTime exactly 1 VoteDate`   <br>
    The VoteObservation has exactly one phenomenon time, represented by a VoteDate.<br>

6.  `Platform hasAPlatformName exactly 1 xsd:string`<br>
   The Platform has exactly one platform name, represented as a string.<br>

7. `VoteType hasADescription exactly 1 xsd:string`<br>
    The VoteType has exactly one description, represented as a string.<br>

8. `VoteType hasAScale exactly 1 xsd:int`<br>
    The VoteType has exactly one scale, represented as an integer.<br>
