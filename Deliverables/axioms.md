**Actor**<br>
     ![actor](../schema-diagrams/Actor/actor.jpg)

Movie SubClassOf providesActorRole only ActorRole<br>
The range of the relationship `providesActorRole` must be `ActorRole`.

providesActorRole some owl:Thing SubClassOf Movie<br>
If something provides an actor role, it must be a `Movie`.

Movie SubClassOf providesActorRole some ActorRole<br>
Every `Movie` must provide at least one `ActorRole`.

ActorRole SubClassOf performsActorRole only Agent<br>
The range of the relationship `performsActorRole` must be `Agent`.

performsActorRole some owl:Thing SubClassOf ActorRole<br>
If something performs an actor role, it must be an `ActorRole`.

ActorRole SubClassOf performsActorRole some Agent<br>
Every `ActorRole` must be performed by an `Agent`.

ActorRole SubClassOf hasTemporalExtent only TemporalExtent<br>
The range of the relationship `hasTemporalExtent` must be `TemporalExtent`.

hasTemporalExtent some owl:Thing SubClassOf ActorRole<br>
If something has a temporal extent, it must be an `ActorRole`.

ActorRole SubClassOf hasTemporalExtent some TemporalExtent<br>
Every `ActorRole` must have a temporal extent specifying time-related details.

LeadRole SubClassOf hasScreenTime only xsd:int<br>
The range of the relationship `hasScreenTime` must be `xsd:int`.

hasScreenTime some owl:Thing SubClassOf LeadRole<br>
If something has screen time, it must be a `LeadRole`.

LeadRole SubClassOf hasScreenTime some xsd:int<br>
Every `LeadRole` must have a screen time represented as an integer.

LeadRole SubClassOf hasFanBase only xsd:String<br>
The range of the relationship `hasFanBase` must be `xsd:String`.

hasFanBase some owl:Thing SubClassOf LeadRole<br>
If something has a fan base, it must be a `LeadRole`.

LeadRole SubClassOf hasFanBase some xsd:String<br>
Every `LeadRole` must have a fan base represented as a string.

SupportingRole SubClassOf hasScreenTime only xsd:int<br>
The range of the relationship `hasScreenTime` must be `xsd:int`.

hasScreenTime some owl:Thing SubClassOf SupportingRole<br>
If something has screen time, it must be a `SupportingRole`.

SupportingRole SubClassOf hasScreenTime some xsd:int<br>
Every `SupportingRole` must have a screen time represented as an integer.

SupportingRole SubClassOf hasBackStory only xsd:String<br>
The range of the relationship `hasBackStory` must be `xsd:String`.

hasBackStory some owl:Thing SubClassOf SupportingRole<br>
If something has a backstory, it must be a `SupportingRole`.

SupportingRole SubClassOf hasBackStory some xsd:String<br>
Every `SupportingRole` must have a backstory represented as a string.

LeadRole SubClassOf ActorRole<br>
`LeadRole` is a subclass of `ActorRole`.

SupportingRole SubClassOf ActorRole<br>
`SupportingRole` is a subclass of `ActorRole`.

LeadRole ⊓ SupportingRole ⊑ ⊥<br>
`LeadRole` and `SupportingRole` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.

ActorRole SubClassOf ∀hasTemporalExtent.TemporalExtent<br>
All objects of the `hasTemporalExtent` relationship for `ActorRole` must be of type `TemporalExtent`

**Budget**<br>
    ![budget](../schema-diagrams/Budget/budget.jpg)

Budget SubClassOf hasQuantityKind only QuantityKind<br>
The range of the relationship `hasQuantityKind` must be `QuantityKind`.

hasQuantityKind some owl:Thing SubClassOf Budget<br>
If something has a `hasQuantityKind` relationship, it must be a `Budget`.

Budget SubClassOf hasQuantityKind some QuantityKind<br>
Every `Budget` must be associated with at least one `QuantityKind`.

Budget SubClassOf hasQuantityValue only QuantityValue<br>
The range of the relationship `hasQuantityValue` must be `QuantityValue`.

hasQuantityValue some owl:Thing SubClassOf Budget<br>
If something has a `hasQuantityValue` relationship, it must be a `Budget`.

Budget SubClassOf hasQuantityValue some QuantityValue<br>
Every `Budget` must have at least one `QuantityValue`.

QuantityValue SubClassOf hasUnit only Unit<br>
The range of the relationship `hasUnit` must be `Unit`.

hasUnit some owl:Thing SubClassOf QuantityValue<br>
If something has a `hasUnit` relationship, it must be a `QuantityValue`.

QuantityValue SubClassOf hasUnit some Unit<br>
Every `QuantityValue` must have a unit associated with it.

QuantityValue SubClassOf hasNumericValue only xsd:double<br>
The range of the relationship `hasNumericValue` must be `xsd:double`.

hasNumericValue some owl:Thing SubClassOf QuantityValue<br>
If something has a `hasNumericValue` relationship, it must be a `QuantityValue`.

QuantityValue SubClassOf hasNumericValue some xsd:double<br>
Every `QuantityValue` must have a numeric value represented as a double.

QuantityKind ⊓ Unit ⊑ ⊥<br>
`QuantityKind` and `Unit` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.

Budget ⊓ QuantityValue ⊑ ⊥<br>
`Budget` and `QuantityValue` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.

QuantityValue SubClassOf ∀hasNumericValue.xsd:double<br>
All objects of the `hasNumericValue` relationship for `QuantityValue` must be of type `xsd:double`.

Budget SubClassOf ⊤<br>
`Budget` is a class that exists as a superclass for other relationships

**Country**<br>
    ![country](../schema-diagrams/Country/country.jpg)

ProductionCompany SubClassOf basedIn only Place<br>
The range of the relationship `basedIn` must be `Place`.

basedIn some owl:Thing SubClassOf ProductionCompany<br>
If something is based in a location, it must be a `ProductionCompany`.

ProductionCompany SubClassOf basedIn some Place<br>
Every `ProductionCompany` must have a base location represented as a `Place`.

Movie SubClassOf hasFilmingLocation only Place<br>
The range of the relationship `hasFilmingLocation` must be `Place`.

hasFilmingLocation some owl:Thing SubClassOf Movie<br>
If something has a filming location, it must be a `Movie`.

Movie SubClassOf hasFilmingLocation some Place<br>
Every `Movie` must have at least one filming location represented by a `Place`.

Place SubClassOf hasCity only City<br>
The range of the relationship `hasCity` must be `City`.

hasCity some owl:Thing SubClassOf Place<br>
If something has a city, it must be a `Place`.

Place SubClassOf hasCity some City<br>
Every `Place` must be associated with at least one `City`.

City SubClassOf hasName only xsd:String<br>
The range of the relationship `hasName` must be `xsd:String`.

hasName some owl:Thing SubClassOf City<br>
If something has a name, it must be a `City`.

City SubClassOf hasName some xsd:String<br>
Every `City` must have a name represented as a string.

Person SubClassOf isACitizenOf only Country<br>
The range of the relationship `isACitizenOf` must be `Country`.

isACitizenOf some owl:Thing SubClassOf Person<br>
If something is a citizen of a country, it must be a `Person`.

Person SubClassOf isACitizenOf some Country<br>
Every `Person` must be a citizen of at least one `Country`.

Country SubClassOf hasCity only City<br>
The range of the relationship `hasCity` must be `City`.

hasCity some owl:Thing SubClassOf Country<br>
If something has a city, it must be a `Country`.

Country SubClassOf hasCity some City Every `Country` must have at least one associated `City`.

City SubClassOf Place<br>
A `City` is a subclass of `Place`.

Country SubClassOf Place<br>
A `Country` is a subclass of `Place`.

City ⊓ Country ⊑ ⊥<br>
`City` and `Country` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.<br>
ProductionCompany ⊓ Movie ⊑ ⊥<br>

`ProductionCompany` and `Movie` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.<br>
City SubClassOf ∀hasName.xsd:String All objects of the `hasName` relationship for `City` must be of type `xsd:String`.<br>

City SubClassOf ∀hasName.xsd:String<br>
All objects of the `hasName` relationship for `City` must be of type `xsd:String`.

**Director**<br>
    ![director](../schema-diagrams/Director/Director.jpg)

Movie SubClassOf providesDirectorRole only DirectorRole<br>
The range of the relationship `providesDirectorRole` must be `DirectorRole`.

providesDirectorRole some owl:Thing SubClassOf Movie<br>
If something provides a `DirectorRole`, it must be a `Movie`.

Movie SubClassOf providesDirectorRole some DirectorRole<br>
Every `Movie` must provide at least one `DirectorRole`.

DirectorRole SubClassOf performsDirectorRole only Agent<br>
The range of the relationship `performsDirectorRole` must be `Agent`.

performsDirectorRole some owl:Thing SubClassOf DirectorRole<br>
If something performs a director role, it must be a `DirectorRole`.

DirectorRole SubClassOf performsDirectorRole some Agent<br>
Every `DirectorRole` must be performed by an `Agent`.

DirectorRole SubClassOf hasTemporalExtent only TemporalExtent<br>
The range of the relationship `hasTemporalExtent` must be `TemporalExtent`.

hasTemporalExtent some owl:Thing SubClassOf DirectorRole<br>
If something has a temporal extent, it must be a `DirectorRole`.

DirectorRole SubClassOf hasTemporalExtent some TemporalExtent<br>
Every `DirectorRole` must have a temporal extent specifying its associated time-related details.

MainDirector SubClassOf hasKeyDecision only xsd:String<br>
The range of the relationship `hasKeyDecision` must be `xsd:String`.

hasKeyDecision some owl:Thing SubClassOf MainDirector<br>
If something has a key decision, it must be a `MainDirector`.

MainDirector SubClassOf hasKeyDecision some xsd:String<br>
Every `MainDirector` must have key decisions represented as strings.

MainDirector SubClassOf hasDirectorialVision only xsd:String<br>
The range of the relationship `hasDirectorialVision` must be `xsd:String`.

hasDirectorialVision some owl:Thing SubClassOf MainDirector<br>
If something has a directorial vision, it must be a `MainDirector`.

MainDirector SubClassOf hasDirectorialVision some xsd:String<br>
Every `MainDirector` must have a directorial vision represented as a string.

TechnicalDirector SubClassOf hasTechnologyUsed only xsd:String<br>
The range of the relationship `hasTechnologyUsed` must be `xsd:String`.

hasTechnologyUsed some owl:Thing SubClassOf TechnicalDirector<br>
If something has technologies used, it must be a `TechnicalDirector`.

TechnicalDirector SubClassOf hasTechnologyUsed some xsd:String<br>
Every `TechnicalDirector` must have technologies used represented as strings.

TechnicalDirector SubClassOf hasTechnicalChallenge only xsd:String<br>
The range of the relationship `hasTechnicalChallenge` must be `xsd:String`.

hasTechnicalChallenge some owl:Thing SubClassOf TechnicalDirector<br>
If something has a technical challenge, it must be a `TechnicalDirector`.

TechnicalDirector SubClassOf hasTechnicalChallenge some xsd:String<br>
Every `TechnicalDirector` must have technical challenges represented as strings.

MainDirector SubClassOf DirectorRole<br>
A `MainDirector` is a subclass of `DirectorRole`.

TechnicalDirector SubClassOf DirectorRole<br>
A `TechnicalDirector` is a subclass of `DirectorRole`.

MainDirector ⊓ TechnicalDirector ⊑ ⊥<br>
`MainDirector` and `TechnicalDirector` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.

**Genre**<br>
 ![genre](../schema-diagrams/Genere/Genere.jpg)

Genre SubClassOf hasTargetAudience only xsd:String<br>
The range of the relationship `hasTargetAudience` must be `xsd:String`.

hasTargetAudience some owl:Thing SubClassOf Genre<br>
If something has a target audience, it must be a `Genre`.

Genre SubClassOf hasTargetAudience some xsd:String<br>
Every `Genre` must have a target audience represented as a string.

Genre SubClassOf hasOrigin only xsd:String<br>
The range of the relationship `hasOrigin` must be `xsd:String`.

hasOrigin some owl:Thing SubClassOf Genre<br>
If something has an origin, it must be a `Genre`.

Genre SubClassOf hasOrigin some xsd:String<br>
Every `Genre` must have an origin represented as a string.

Comedy SubClassOf Genre<br>
A `Comedy` is a subclass of `Genre`.

Action SubClassOf Genre<br>
An `Action` is a subclass of `Genre`.

Horror SubClassOf Genre<br>
A `Horror` is a subclass of `Genre`.

DarkComedy SubClassOf Comedy<br>
`DarkComedy` is a subclass of `Comedy`.

Satire SubClassOf Comedy<br>
`Satire` is a subclass of `Comedy`.

MartialArts SubClassOf Action<br>
`MartialArts` is a subclass of `Action`.

Superhero SubClassOf Action<br>
`Superhero` is a subclass of `Action`.

MonsterHorror SubClassOf Horror<br>
`MonsterHorror` is a subclass of `Horror`.

Slasher SubClassOf Horror<br>
`Slasher` is a subclass of `Horror`.

Comedy ⊓ Action ⊑ ⊥<br>
`Comedy` and `Action` are disjoint classes, meaning an entity cannot belong to both classes simultaneously.

Comedy ⊓ Horror ⊑ ⊥<br>
`Comedy` and `Horror` are disjoint classes.

Action ⊓ Horror ⊑ ⊥<br>
`Action` and `Horror` are disjoint classes.

DarkComedy ⊓ Satire ⊑ ⊥<br>
`DarkComedy` and `Satire` are disjoint subclasses of `Comedy`.

MartialArts ⊓ Superhero ⊑ ⊥<br>
`MartialArts` and `Superhero` are disjoint subclasses of `Action`.

MonsterHorror ⊓ Slasher ⊑ ⊥<br>
`MonsterHorror` and `Slasher` are disjoint subclasses of `Horror`.

Genre SubClassOf ≤1hasTargetAudience<br>
Each `Genre` can have at most one `hasTargetAudience` relationship.

Genre SubClassOf ≤1hasOrigin<br>
Each `Genre` can have at most one `hasOrigin` relationship.

Comedy SubClassOf hasTargetAudience some xsd:String<br>
Every `Comedy` genre must have a target audience.

Action SubClassOf hasOrigin some xsd:String<br>
Every `Action` genre must have an origin.

Horror SubClassOf hasTargetAudience some xsd:String<br>
Every `Horror` genre must have a target audience.


**GrossEarning**<br>
    ![grossEarning](../schema-diagrams/GrossEarning/grossEarning.jpg)

GrossEarnings SubClassOf hasEarningsValue only EarningsValue<br>
The range of the relationship `hasEarningsValue` must be `EarningsValue`.

hasEarningsValue some owl:Thing SubClassOf GrossEarnings<br>
If something has an earnings value, it must be a `GrossEarnings`.

GrossEarnings SubClassOf hasEarningsValue some EarningsValue<br>
Every `GrossEarnings` must have at least one associated `EarningsValue`.

GrossEarnings SubClassOf hasEarningsType only EarningsType<br>
The range of the relationship `hasEarningsType` must be `EarningsType`.

hasEarningsType some owl:Thing SubClassOf GrossEarnings<br>
If something has an earnings type, it must be a `GrossEarnings`.

GrossEarnings SubClassOf hasEarningsType some EarningsType<br>
Every `GrossEarnings` must have an associated `EarningsType`.

EarningsValue SubClassOf hasNumericValue only xsd:int<br>
The range of the relationship `hasNumericValue` must be `xsd:int`.

hasNumericValue some owl:Thing SubClassOf EarningsValue<br>
If something has a numeric value, it must be an `EarningsValue`.

EarningsValue SubClassOf hasNumericValue some xsd:int<br>
Every `EarningsValue` must have a numeric value represented as an integer.

EarningsValue SubClassOf hasCurrency only Currency<br>
The range of the relationship `hasCurrency` must be `Currency`.

hasCurrency some owl:Thing SubClassOf EarningsValue<br>
If something has a currency, it must be an `EarningsValue`.

EarningsValue SubClassOf hasCurrency some Currency<br>
Every `EarningsValue` must have an associated `Currency`.

**MovieRating**<br>
    ![grossEarning](../schema-diagrams/MovieRating/movieRating.png)

MovieRatingObservation SubClassOf observedProperty only Rating<br>
The range of the relationship `observedProperty` must be `Rating`.

observedProperty some owl:Thing SubClassOf MovieRatingObservation<br>
If something observes a property, it must be a `MovieRatingObservation`.

MovieRatingObservation SubClassOf observedProperty some Rating<br>
Every `MovieRatingObservation` must observe at least one `Rating`.

MovieRatingObservation SubClassOf hasSimpleResult only rdfs:NumericUserRatingValue<br>
The range of the relationship `hasSimpleResult` must be `rdfs:NumericUserRatingValue`.

hasSimpleResult some owl:Thing SubClassOf MovieRatingObservation<br>
If something has a simple result, it must be a `MovieRatingObservation`.

MovieRatingObservation SubClassOf hasSimpleResult some rdfs:NumericUserRatingValue<br>
Every `MovieRatingObservation` must have a simple result represented as a numeric user rating value.

MovieRatingObservation SubClassOf hasPhenomenonTime only RatingDate<br>
The range of the relationship `hasPhenomenonTime` must be `RatingDate`.

MovieRatingObservation SubClassOf hasResultTime only RatingDate<br>
The range of the relationship `hasResultTime` must be `RatingDate`.

hasPhenomenonTime some owl:Thing SubClassOf MovieRatingObservation<br>
If something has a phenomenon time, it must be a `MovieRatingObservation`.

hasResultTime some owl:Thing SubClassOf MovieRatingObservation<br>
If something has a result time, it must be a `MovieRatingObservation`.

MovieRatingObservation SubClassOf hasPhenomenonTime some RatingDate and hasResultTime some RatingDate<br>
Every `MovieRatingObservation` must have a phenomenon time and a result time represented as a `RatingDate`.

⊤ SubClassOf ≤1hasPhenomenonTime<br>
Each `MovieRatingObservation` can have at most one `hasPhenomenonTime` relationship.

MovieRatingObservation SubClassOf hasResult only RatingValue<br>
The range of the relationship `hasResult` must be `RatingValue`.

hasResult some owl:Thing SubClassOf MovieRatingObservation<br>
If something has a result, it must be a `MovieRatingObservation`.

MovieRatingObservation SubClassOf hasResult some RatingValue<br>
Every `MovieRatingObservation` must have a result represented by a `RatingValue`.

MovieRatingObservation SubClassOf hasObservedMovie only Movie<br>
The range of the relationship `hasObservedMovie` must be `Movie`.

hasObservedMovie some owl:Thing SubClassOf MovieRatingObservation<br>
If something observes a movie, it must be a `MovieRatingObservation`.

MovieRatingObservation SubClassOf hasObservedMovie some Movie<br>
Every `MovieRatingObservation` must be associated with at least one observed `Movie`.

Platform SubClassOf hasAPlatformName only xsd:String<br>
The range of the relationship `hasAPlatformName` must be `xsd:String`.

hasAPlatformName some owl:Thing SubClassOf Platform<br>
If something has a platform name, it must be a `Platform`.

Platform SubClassOf hasAPlatformName some xsd:String<br>
Every `Platform` must have a name represented as a string.


**ProducationCompany**<br>
    ![grossEarning](../schema-diagrams/ProductionCompany/ProductionCompanies.jpg)

Movie SubClassOf providesProductionRole only ProductionRole<br>
The range of the relationship `providesProductionRole` must be `ProductionRole`.

providesProductionRole some owl:Thing SubClassOf Movie<br>
If something provides a production role, it must be a `Movie`.

Movie SubClassOf providesProductionRole some ProductionRole<br>
Every `Movie` must provide at least one `ProductionRole`.

ProductionRole SubClassOf hasTemporalExtent only ProductionPeriod<br>
The range of the relationship `hasTemporalExtent` must be `ProductionPeriod`.

hasTemporalExtent some owl:Thing SubClassOf ProductionRole<br>
If something has a temporal extent, it must be a `ProductionRole`.

ProductionRole SubClassOf hasTemporalExtent some ProductionPeriod<br>
Every `ProductionRole` must have a temporal extent specifying its associated `ProductionPeriod`.

ProductionRole SubClassOf performedBy only Agent<br>
The range of the relationship `performedBy` must be `Agent`.

performedBy some owl:Thing SubClassOf ProductionRole<br>
If something is performed by an agent, it must be a `ProductionRole`.

ProductionRole SubClassOf performedBy some Agent<br>
Every `ProductionRole` must be performed by an `Agent`.

ExecutiveProducer SubClassOf hasFinancialContribution only xsd:int<br>
The range of the relationship `hasFinancialContribution` must be `xsd:int`.

hasFinancialContribution some owl:Thing SubClassOf ExecutiveProducer<br>
If something has a financial contribution, it must be an `ExecutiveProducer`.

ExecutiveProducer SubClassOf hasFinancialContribution some xsd:int<br>
Every `ExecutiveProducer` must have a financial contribution represented as an integer.

ExecutiveProducer SubClassOf hasCreativeControl only xsd:String<br>
The range of the relationship `hasCreativeControl` must be `xsd:String`.

hasCreativeControl some owl:Thing SubClassOf ExecutiveProducer<br>
If something has creative control, it must be an `ExecutiveProducer`.

ExecutiveProducer SubClassOf hasCreativeControl some xsd:String<br>
Every `ExecutiveProducer` must have creative control represented as a string.

ExecutiveProducer SubClassOf hasContractTerms only xsd:int<br>
The range of the relationship `hasContractTerms` must be `xsd:int`.

hasContractTerms some owl:Thing SubClassOf ExecutiveProducer<br>
If something has contract terms, it must be an `ExecutiveProducer`.

ExecutiveProducer SubClassOf hasContractTerms some xsd:int<br>
Every `ExecutiveProducer` must have contract terms represented as an integer.

Distribution SubClassOf hasRevenueSharePercentage only xsd:int<br>
The range of the relationship `hasRevenueSharePercentage` must be `xsd:int`.

hasRevenueSharePercentage some owl:Thing SubClassOf Distribution<br>
If something has a revenue share percentage, it must be a `Distribution`.

Distribution SubClassOf hasRevenueSharePercentage some xsd:int<br>
Every `Distribution` must have a revenue share percentage represented as an integer.

Distribution SubClassOf hasDistributionRegion only xsd:String<br>
The range of the relationship `hasDistributionRegion` must be `xsd:String`.

hasDistributionRegion some owl:Thing SubClassOf Distribution<br>
If something has a distribution region, it must be a `Distribution`.

Distribution SubClassOf hasDistributionRegion some xsd:String<br>
Every `Distribution` must have a distribution region represented as a string.

Distribution SubClassOf hasReleasePlatforms only xsd:String<br>
The range of the relationship `hasReleasePlatforms` must be `xsd:String`.

hasReleasePlatforms some owl:Thing SubClassOf Distribution<br>
If something has release platforms, it must be a `Distribution`.

Distribution SubClassOf hasReleasePlatforms some xsd:String<br>
Every `Distribution` must have release platforms represented as a string.

**InflationRate**<br>
    ![InflationRate](../schema-diagrams/InflationRate/inflationRate.jpg)

InflationObservation SubClassOf contains only InflationTimeExtent<br>
The range of the relationship `contains` must be `InflationTimeExtent`.

contains some owl:Thing SubClassOf InflationObservation<br>
If something contains an inflation time extent, it must be an `InflationObservation`.

InflationObservation SubClassOf contains some InflationTimeExtent<br>
Every `InflationObservation` must contain at least one `InflationTimeExtent`.

InflationTimeExtent SubClassOf hasDuration only ObservationPeriod<br>
The range of the relationship `hasDuration` must be `ObservationPeriod`.

hasDuration some owl:Thing SubClassOf InflationTimeExtent<br>
If something has a duration, it must be an `InflationTimeExtent`.

InflationTimeExtent SubClassOf hasDuration some ObservationPeriod<br>
Every `InflationTimeExtent` must have a duration represented by an `ObservationPeriod`.

ObservationPeriod SubClassOf startsFrom only ReleaseDate<br>
The range of the relationship `startsFrom` must be `ReleaseDate`.

ObservationPeriod SubClassOf endsAt only ReleaseDate<br>
The range of the relationship `endsAt` must be `ReleaseDate`.

startsFrom some owl:Thing SubClassOf ObservationPeriod<br>
If something has a starting point, it must be an `ObservationPeriod`.

endsAt some owl:Thing SubClassOf ObservationPeriod<br>
If something has an ending point, it must be an `ObservationPeriod`.

ObservationPeriod SubClassOf startsFrom some ReleaseDate and endsAt some ReleaseDate<br>
Every `ObservationPeriod` must have a starting and an ending point represented by `ReleaseDate`.

InflationTimeExtent SubClassOf hasValue only InflationRateValue<br>
The range of the relationship `hasValue` must be `InflationRateValue`.

hasValue some owl:Thing SubClassOf InflationTimeExtent<br>
If something has a value, it must be an `InflationTimeExtent`.

InflationTimeExtent SubClassOf hasValue some InflationRateValue<br>
Every `InflationTimeExtent` must have a value represented by an `InflationRateValue`.

InflationRateValue SubClassOf hasPercentage only xsd:double<br>
The range of the relationship `hasPercentage` must be `xsd:double`.

hasPercentage some owl:Thing SubClassOf InflationRateValue<br>
If something has a percentage, it must be an `InflationRateValue`.

InflationRateValue SubClassOf hasPercentage some xsd:double<br>
Every `InflationRateValue` must have a percentage represented as a double.

ReleaseDate SubClassOf hasReferenceSystem only CurrencyReferenceSystem<br>
The range of the relationship `hasReferenceSystem` must be `CurrencyReferenceSystem`.

hasReferenceSystem some owl:Thing SubClassOf ReleaseDate<br>
If something has a reference system, it must be a `ReleaseDate`.

ReleaseDate SubClassOf hasReferenceSystem some CurrencyReferenceSystem<br>
Every `ReleaseDate` must have a reference system associated with a `CurrencyReferenceSystem`.


**UserRating**<br>
    ![grossEarning](../schema-diagrams/UserRating/userRatings.jpg)

UserRatingObservation SubClassOf observedProperty only RatingType<br>
The range of the relationship `observedProperty` must be `RatingType`.

observedProperty some owl:Thing SubClassOf UserRatingObservation<br>
If something has an `observedProperty`, it must be a `UserRatingObservation`.

UserRatingObservation SubClassOf observedProperty some RatingType<br>
Every `UserRatingObservation` must observe at least one `RatingType`.

UserRatingObservation SubClassOf hasSimpleResult only rdfs:NumericRatingValue<br>
The range of the relationship `hasSimpleResult` must be `rdfs:NumericRatingValue`.

hasSimpleResult some owl:Thing SubClassOf UserRatingObservation<br>
If something has a `hasSimpleResult` relationship, it must be a `UserRatingObservation`.

UserRatingObservation SubClassOf hasSimpleResult some rdfs:NumericRatingValue<br>
Every `UserRatingObservation` must have a simple result as a numeric rating value.

UserRatingObservation SubClassOf hasResultTime only RatingDate<br>
The range of the relationship `hasResultTime` must be `RatingDate`.

hasResultTime some owl:Thing SubClassOf UserRatingObservation<br>
If something has a `hasResultTime` relationship, it must be a `UserRatingObservation`.

UserRatingObservation SubClassOf hasResultTime some RatingDate<br>
Every `UserRatingObservation` must have a result time as a `RatingDate`.

UserRatingObservation SubClassOf hasResultTime max 1 RatingDate<br>
Each `UserRatingObservation` can have at most one `hasResultTime` relationship.

UserRatingObservation SubClassOf hasResult only RatingValue<br>
The range of the relationship `hasResult` must be `RatingValue`.

hasResult some owl:Thing SubClassOf UserRatingObservation<br>
If something has a `hasResult` relationship, it must be a `UserRatingObservation`.

UserRatingObservation SubClassOf hasResult some RatingValue<br>
Every `UserRatingObservation` must have a result represented by a `RatingValue`.

UserRatingObservation SubClassOf hasObservedMovie only Movie<br>
The range of the relationship `hasObservedMovie` must be `Movie`.

hasObservedMovie some owl:Thing SubClassOf UserRatingObservation<br>
If something has a `hasObservedMovie` relationship, it must be a `UserRatingObservation`.

UserRatingObservation SubClassOf hasObservedMovie some Movie<br>
Every `UserRatingObservation` must observe at least one `Movie`.

Platform SubClassOf hasAPlatformName only xsd:String<br>
The range of the relationship `hasAPlatformName` must be `xsd:String`.

hasAPlatformName some owl:Thing SubClassOf Platform<br>
If something has a `hasAPlatformName` relationship, it must be a `Platform`.

Platform SubClassOf hasAPlatformName some xsd:String<br>
Every `Platform` must have a platform name represented as a string.

RatingType SubClassOf hasADescription only xsd:String<br>
The range of the relationship `hasADescription` must be `xsd:String`.

hasADescription some owl:Thing SubClassOf RatingType<br>
If something has a `hasADescription` relationship, it must be a `RatingType`.

RatingType SubClassOf hasADescription some xsd:String<br>
Every `RatingType` must have a description represented as a string.

RatingType SubClassOf hasMaxScale only xsd:int<br>
The range of the relationship `hasMaxScale` must be `xsd:int`.

hasMaxScale some owl:Thing SubClassOf RatingType<br>
If something has a `hasMaxScale` relationship, it must be a `RatingType`.

RatingType SubClassOf hasMaxScale some xsd:int<br>
Every `RatingType` must have a maximum scale represented as an integer.



**Vote**<br>
    ![grossEarning](../schema-diagrams/Vote/vote.jpg)

`VoteObservation SubClassOf observedProperty only VoteType`<br>
The range of the relationship `observedProperty` must be `VoteType`.<br>

`observedProperty some owl:Thing SubClassOf VoteObservation`<br>
If something has an observed property, it must be a `VoteObservation`.<br>

`VoteObservation SubClassOf observedProperty some VoteType`<br>
Every `VoteObservation` must observe at least one `VoteType`.<br>

`VoteObservation SubClassOf hasSimpleResult only rdfs:NumericVoteValue`<br>
The range of the relationship `hasSimpleResult` must be `rdfs:NumericVoteValue`.<br>

`hasSimpleResult some owl:Thing SubClassOf VoteObservation`<br>
If something has a simple result, it must be a `VoteObservation`.<br>

`VoteObservation SubClassOf hasSimpleResult some rdfs:NumericVoteValue`<br>
Every `VoteObservation` must have a simple result.<br>

`VoteObservation SubClassOf hasPhenomenonTime only VoteDate`<br>
The range of the relationship `hasPhenomenonTime` must be `VoteDate`.<br>

`hasPhenomenonTime some owl:Thing SubClassOf VoteObservation`<br>
If something has a phenomenon time, it must be a `VoteObservation`.<br>

`VoteObservation SubClassOf hasPhenomenonTime some VoteDate`<br>
Every `VoteObservation` must have a phenomenon time.<br>

`VoteObservation SubClassOf hasPhenomenonTime max 1 VoteDate`<br>
Each `VoteObservation` can have at most one phenomenon time.<br>

`VoteObservation SubClassOf hasResult only VoteCount`<br>
The range of the relationship `hasResult` must be `VoteCount`.<br>

`hasResult some owl:Thing SubClassOf VoteObservation`<br>
If something has a result, it must be a `VoteObservation`.<br>

`VoteObservation SubClassOf hasResult some VoteCount`<br>
Every `VoteObservation` must have a result.<br>

`VoteObservation SubClassOf hasFeatureOfInterest only Movie`<br>
The range of the relationship `hasFeatureOfInterest` must be `Movie`.<br>

`hasFeatureOfInterest some owl:Thing SubClassOf VoteObservation`<br>
If something has a feature of interest, it must be a `VoteObservation`.<br>

`VoteObservation SubClassOf hasFeatureOfInterest some Movie`<br>
Every `VoteObservation` must have a feature of interest.<br>

`Platform SubClassOf hasAPlatformName only xsd:String`<br>
The range of the relationship `hasAPlatformName` must be `xsd:String`.<br>

`hasAPlatformName some owl:Thing SubClassOf Platform`<br>
If something has a platform name, it must be a `Platform`.<br>

`Platform SubClassOf hasAPlatformName some xsd:String`<br>
Every `Platform` must have a platform name.<br>

`VoteType SubClassOf hasADescription only xsd:String`<br>
<br>
The range of the relationship `hasADescription` must be `xsd:String`.<br>

`hasADescription some owl:Thing SubClassOf VoteType`<br>
If something has a description, it must be a `VoteType`.<br>

`VoteType SubClassOf hasADescription some xsd:String`<br>
Every `VoteType` must have a description.<br>

`VoteType SubClassOf hasAScale only xsd:int`<br>
The range of the relationship `hasAScale` must be `xsd:int`.<br>

`hasAScale some owl:Thing SubClassOf VoteType`<br>
If something has a scale, it must be a `VoteType`.<br>

`VoteType SubClassOf hasAScale some xsd:int`<br>
Every `VoteType` must have a scale.<br>

