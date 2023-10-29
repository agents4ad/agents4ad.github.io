---
layout: splash
header:
  overlay_color: "#5e616c"
  overlay_filter: "0.5"
  overlay_image: assets/images/header_from_unsplash_dot_com.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
title: 'Workshop on Traffic Agent Modeling for Autonomous Driving Simulation'
excerpt: 'An IEEE/RSJ IROS 2023 workshop.'

organizers_row:
  - image_path: assets/images/organizers/maximilian_naumann.jpeg
    alt: "Max"
    person_name: "Maximilian Naumann"
    person_affiliation: "Bosch Center for Artifical Intelligence and KIT"
  - image_path: assets/images/organizers/max_igl.jpg
    alt: "Max"
    person_name: "Maximilian Igl"
    person_affiliation: "Waymo Research"
  - image_path: assets/images/organizers/simon_suo.jpeg
    alt: "Simon"
    person_name: "Simon Suo"
  - image_path: assets/images/organizers/thomas_gilles.jpeg
    alt: "Thomas"
    person_name: "Thomas Gilles"
    person_affiliation: "Waabi and MINES Paris - PSL"
  - image_path: assets/images/organizers/yiren_lu.jpeg
    alt: "Yiren"
    person_name: "Yiren Lu"
    person_affiliation: "Waymo Research"
  - image_path: assets/images/organizers/fabien_moutarde.jpeg
    alt: "Fabien"
    person_name: "Fabien Moutarde"
    person_affiliation: "MINES Paris - PSL"
  - image_path: assets/images/organizers/anca_dragan.jpeg
    alt: "Anca"
    person_name: "Anca Dragan"
    person_affiliation: "UC Berkeley"
  - image_path: assets/images/organizers/shimon_whiteson.jpeg
    alt: "Shimon"
    person_name: "Shimon Whiteson"
    person_affiliation: "Waymo UK and University of Oxford"

schedule:
  - time: "08:30"
    event: "Welcome"
    content: 
  - time: "08:45"
    image_path: assets/images/speakers/maria_soledad_elli.png
    person_name: "Maria Soledad Elli"
    person_affiliation: "Data Scientist, Intel"
    content: "Operational Safety Assessment of Automated Vehicles in Simulation"
  - time: "09:05"
    image_path: assets/images/speakers/alyssa_pierson.png
    person_name: "Alyssa Pierson"
    person_affiliation: "Assistant Professor, Boston University"
    content: "[Modeling Interactions within Multi-Agent Autonomous Driving](https://youtu.be/UrEwanmAWmk)"
  - time: "09:25"
    image_path: assets/images/speakers/holger_caesar.png
    person_name: "Holger Caesar"
    person_affiliation: "Assistant Professor, TU Delft"
    content: "[ML-based traffic agent simulation with nuPlan](https://youtu.be/aie3uj6jHKY)"
  - time: "09:45"
    event: "Spotlight presentations of posters"
    content: 
  - time: "10:00"
    event: "Coffee break and poster session 1"
    content: 
  - time: "11:00"
    image_path: assets/images/speakers/henggang_cui.png
    person_name: "Henggang Cui"
    person_affiliation: "Principal Engineer, Prediction Team Lead at Motional"
    content: "[Trajectory prediction for real-world autonomous driving](https://youtu.be/UZJqyJ3Lpu8)"
  - time: "11:20"
    image_path: assets/images/speakers/jonah_philion.png
    person_name: "Jonah Philion"
    person_affiliation: "Research Scientist, NVIDIA <br>PhD Student, U. of Toronto"
    content: "[Traffic Modeling: Data as Expert vs. Data as Environment](https://youtu.be/NBxs51ePlcw)"
  - time: "11:40"
    image_path: assets/images/speakers/marco_pavone.png
    person_name: "Marco Pavone"
    person_affiliation: "Director AV Research, NVIDIA <br> Associate Professor, Stanford University"
    content: "[Generative AI for Diverse and Controllable AV Simulation](https://www.youtube.com/watch?v=cpvjIKUHCV4)"
  - time: "12:10"
    event: "Lunch break"
    content: 
  - time: "13:30"
    image_path: assets/images/speakers/nico_montali.png
    person_name: "Nico Montali"
    person_affiliation: Research Engineer, Waymo
    second_image_path: assets/images/speakers/john_lambert.png
    second_person_name: "John Lambert"
    second_person_affiliation: "Research Scientist, Waymo"
    content: "Waymo's Sim Agents Challenge: How to evaluate agent quality?"
  - time: "14:00"
    image_path: assets/images/speakers/eric_wolff.png
    person_name: "Eric Wolff"
    person_affiliation: "Research Scientist, Behavior Research Lead, Cruise"
    content: "[Scaling the Robotaxi](https://youtu.be/lvEdH_K9pmg)"
  - time: "14:30"
    image_path: assets/images/speakers/chris_zhang.png
    person_name: "Chris Zhang"
    person_affiliation: "Research Scientist, Waabi"
    second_image_path: assets/images/speakers/kelvin_wong.png
    second_person_name: "Kelvin Wong"
    second_person_affiliation: "Research Scientist, Waabi"
    content: "Traffic Modeling for Closed-loop Simulation"
  - time: "15:00"
    event: "Coffee break and poster session 2"
    content: 
  - time: "16:00"
    image_path: assets/images/speakers/tianyu_tang.png
    person_name: "Tianyu Tang"
    person_affiliation: "PhD Student, TU Munich"
    content: "What information do humans base their (traffic) behavior decision on - insights from ergonomics"
  - time: "16:20"
    image_path: assets/images/speakers/thomas_lich.png
    person_name: "Thomas Lich"
    person_affiliation: "Senior Expert and Team Lead, Bosch Accident Research"
    content: "[Raising attention to underrepresented entities in simulation studies - a perspective from accident research and two-wheeler research](https://www.youtube.com/watch?v=TtkuwlI8DXs)"
  - time: "16:40"
    event: "Panel Discussion"
    content: 
  - time: "17:25"
    event: "Closing remarks"
    content: 

papers: 
  - title: Can you text what is happening? Integrating pretrained language encoders into trajectory prediction models for autonomous driving
    authors: Ali Keysan, Andreas Look, Eitan Kosman, Gonca Gürsun, Jörg Wagner, Yu Yao, Barbara Rakitsch
    video: https://player.vimeo.com/video/867619642?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
    poster: Link to pdf
    pdf: Link to pdf
    abstract: "In autonomous driving tasks, scene understanding is the first step towards predicting the future behavior of the surrounding traffic participants. Yet, how to represent a given scene and extract its features are still open research questions. In this study, we propose a novel text-based representation of traffic scenes and process it with a pre-trained language encoder. First, we show that text-based representations, combined with classical rasterized image representations, lead to descriptive scene embeddings. Second, we benchmark our predictions on the nuScenes dataset and show significant improvements compared to baselines. Third, we show in an ablation study that a joint encoder of text and rasterized images outperforms the individual encoders confirming that both representations have their complementary strengths."
  - title: Differentiable Constrained Imitation Learning for Robot Motion Planning and Control
    authors: Christopher Diehl, Janis Adamek, Martin Krueger, Frank Hoffmann, Torsten Bertram 
    video: https://player.vimeo.com/video/867619650?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
    poster: Link to pdf
    pdf: Link to pdf
    abstract: "Motion planning and control are crucial components of robotics applications like automated driving. Here, spatio-temporal hard constraints like system dynamics and safety boundaries (e.g., obstacles) restrict the robot's motions. Direct methods from optimal control solve a constrained optimization problem. However, in many applications finding a proper cost function is inherently difficult because of the weighting of partially conflicting objectives. On the other hand, Imitation Learning (IL) methods such as Behavior Cloning (BC) provide an intuitive framework for learning decision-making from offline demonstrations and constitute a promising avenue for planning and control in complex robot applications. Prior work primarily relied on soft constraint approaches, which use additional auxiliary loss terms describing the constraints. However, catastrophic safety-critical failures might occur in out-of-distribution (OOD) scenarios. This work integrates the flexibility of IL with hard constraint handling in optimal control. Our approach constitutes a general framework for constraint robotic motion planning and control, as well as traffic agent simulation, whereas we focus on mobile robot and automated driving applications. Hard constraints are integrated into the learning problem in a differentiable manner, via explicit completion and gradient-based correction. Simulated experiments of mobile robot navigation and automated driving provide evidence for the performance of the proposed method." 
  - title: Simulation-based evaluation of a generic Autonomous Emergency Braking system using a cognitive pedestrian behavior model
    authors: Lucas Fonseca Alexandre de Oliveira, Lukas Brostek, Martin Meywerk
    video: https://player.vimeo.com/video/867619659?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479
    poster: Link to pdf
    pdf: Link to pdf
    abstract: "In 2020 pedestrians accounted for 21,4% of all deaths in the European Union. Considering all vulnerable road users (VRU: pedestrians, cyclists, motorcycles, and mopeds) they accounted for 51,4% of all deaths. To reduce the number of deaths and improve VRU safety, systems have been developed in the last decades. The autonomous emergency braking system (AEB) is one of these systems and aims to intervene in conflict situations by applying an emergency braking (in some cases only after the driver starts the brake itself). The performance evaluation of an AEB system via simulation reduces cost and time against real tests and allows better robustness evaluation because of the higher number of scenarios that can be simulated. In the virtual-world, safety-critical situations can also be tested without any problems. The modeling of pedestrian behavior plays an important role since the pedestrian is the vehicle's adversary in this context. Current studies use a simple pedestrian model, in which the pedestrian does not have any perception of the environment, moving on a pre-defined path with constant speed. Such trajectory-based models are available in the most common vehicle dynamic simulation tools. In reality, however, pedestrian usually react to the approaching vehicle in conflict situations by adjusting their trajectory, which can change the conflict situation and affect the performance assessment of AEB systems. This study compares the standard model with neuro-cognitive pedestrian model from cogniBIT and investigates if and how these models affect the performance assessment of AEB systems."

---

This workshop will be held at the [IEEE/RSJ IROS 2023](https://ieee-iros.org/), on **October 5th, 2023, in Room 140E** at Huntington Place, Detroit, MI, USA and **[streamed online (via zoom)](https://waabi-ai.zoom.us/j/81205991343?pwd=ZsbHwbjhlWevb7m3Be0q7Peon3YbV1.1)**.

## Abstract

Simulation is a crucial tool to accelerate the development of Autonomous Driving (AD) algorithms. Realistic traffic agent models reduce the sim-to-real gap and have the potential to massively scale evaluation of AD algorithms, paying into both development and safe deployment of AD systems.

Research in traffic agent modeling has recently made great advances, for example due to the switch to graph neural networks and training through sequential decisions. Yet, the research is scattered over different robotics and machine learning venues.

This workshop shall provide a platform to highlight recent advances and future directions towards realistic traffic agent models. Furthermore, this workshop shall provide insights from related fields such as prediction, motion planning and AV safety. Through a mix of invited talks from both academia and industry, paper presentations, and a panel discussion, attendees will be able to catch up with the latest advances, promising directions and most pressing challenges. Attendees will also be able to network in this growing field of research and related areas.

## Location

On site: **Room 140E** at Huntington Place, Detroit, MI, USA.

Online: [streamed via zoom](https://waabi-ai.zoom.us/j/81205991343?pwd=ZsbHwbjhlWevb7m3Be0q7Peon3YbV1.1).

## Agenda

<!-- script to display conference time -->
<script>
  var x = setInterval(function() {
    var d = new Date();
    var n = d.toLocaleTimeString("en-US", {timeZone: "America/Detroit", hour: '2-digit', minute:'2-digit', hour12: false})
    document.getElementById("centraltime").innerHTML = n
  }, 1000);
</script>

This full day workshop will take place on Thursday Oct 5th, 08:30 to 17:30 EDT (UTC-4). [ICS-file](assets/TAM-Workshop.ics).

Below times are in Detroit time. Current time in Detroit is <span id="centraltime"></span>.

{% include schedule %}

## Invited Speakers

{% include feature_row id="schedule" %}

## Papers

{% include papers %}

## Organizers

{% include feature_row id="organizers_row" %}

Contact: [agents4ad@googlegroups.com](mailto:agents4ad@googlegroups.com)

## Support

This workshop is supported by the

- IEEE RAS Technical Committee on Algorithms for Planning and Control of Robot Motion
- IEEE RAS Technical Committee on Autonomous Ground Vehicles and Intelligent Transportation Systems
- IEEE ITSS Technical Committee on Self-Driving Automobiles
