![actor](../schema-diagrams/Actor/actor.png)

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
