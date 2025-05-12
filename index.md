---
layout: splash
header:
  overlay_color: "#5e616c"
  overlay_filter: "0.5"
  overlay_image: assets/images/header_from_unsplash_dot_com.jpg
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
title: 'Workshop on Data-Driven Autonomous Driving Simulation (DDADS)'
excerpt: 'A CVPR 2025 workshop.'

organizers_row:
  - image_path: assets/images/organizers/azadeh_dinparastdjadid.jpg
    alt: ""
    person_name: "Azadeh Dinparastdjadid"
    person_affiliation: "Waymo"
  - image_path: https://zgojcic.github.io/assets/Profile_picutre_ZG_crop.jpg
    alt: ""
    person_name: "Zan Gojcic"
    person_affiliation: "NVIDIA"
  - image_path: assets/images/organizers/max_igl.jpg
    alt: "Max"
    person_name: "Maximilian Igl"
    person_affiliation: "NVIDIA"
  - image_path: assets/images/organizers/maximilian_naumann.jpeg
    alt: "Max"
    person_name: "Maximilian Naumann"
    person_affiliation: "Bosch Center for Artificial Intelligence and KIT"
  - image_path: assets/images/organizers/thomas_gilles.jpeg
    alt: "Thomas"
    person_name: "Thomas Gilles"
    person_affiliation: "Waabi"
  - image_path: assets/images/organizers/kate_tolstaya.jpg
    alt: "Kate"
    person_name: "Kate Tolstaya"
    person_affiliation: "Waymo"
  - image_path: assets/images/organizers/sanja_fidler.jpg
    alt: ""
    person_name: "Sanja Fidler"
    person_affiliation: "NVIDIA and University of Toronto"
  - image_path: assets/images/organizers/shimon_whiteson.jpeg
    alt: "Shimon"
    person_name: "Shimon Whiteson"
    person_affiliation: "Waymo UK and University of Oxford"

schedule:
  - time: "8:30"
    event: "Welcome"
    content: 
  - time: "8:45"
    image_path: https://ai.stanford.edu/~cbfinn/_files/sail_headshot_left_facing_crop.jpg
    person_name: "Chelsea Finn"
    person_affiliation: "Stanford University"
    content: "Leveraging Synthetic Data for Robot Training and Evaluation"
  - time: "9:15"
    image_path: https://www.princeton.edu/sites/default/files/styles/scale_1440/public/images/2022/10/FelixHeide-062821_0022_sq1023.jpg?itok=Ph2ZT13W
    person_name: "Felix Heide"
    person_affiliation: "Torc Robotics & Princeton University"
    content: "Learning to Plan with Self-Play: Fully Data-driven Generative Scenarios for Autonomous Driving"
  - time: "9:45"
    event: "Poster Presentations 1"
    content: 
  - time: "10:15"
    event: "Coffee & Posters"
    content: 
  - time: "11:00"
    image_path: https://scholar.googleusercontent.com/citations?view_op=view_photo&user=HKfLbg0AAAAJ&citpid=2
    person_name: "Johan Engstrom"
    person_affiliation: "Waymo"
    content: "Understanding and modeling of human driver behavior based on active inference"
  - time: "11:30"
    image_path: assets/images/speakers/marco_pavone.jpeg
    person_name: "Marco Pavone"
    person_affiliation: "NVIDIA & Stanford University"
    content: "tbd"
  - time: "12:00"
    event: "Lunch Break"
    content: 
  - time: "14:00"
    image_path: https://d2xo500swnpgl1.cloudfront.net/uploads/scale/Draogmir-Anguelov-1633527577257.png
    person_name: "Dragomir Anguelov"
    person_affiliation: "Waymo"
    content: "tbd"
  - time: "14:30"
    event: "Poster Presentations 2"
    content: 
  - time: "15:15"
    event: "Coffee & Posters"
    content: 
  - time: "16:00"
    image_path: https://www.eugenevinitsky.com/images/eugene.jpg
    person_name: "Eugene Vinitsky"
    person_affiliation: "New York University"
    content: "Robust Self-Driving Emerges from Self-Play"
  - time: "16:30"
    image_path: assets/images/speakers/raquel_urtasun.png
    person_name: "Raquel Urtasun"
    person_affiliation: "Waabi"
    content: "tbd"
  - time: "17:00"
    event: "Panel Discussion (moderated by Sanja Fidler)"
    content: 
  - time: "17:45"
    event: "Closing remarks"
    content: 


---

This workshop will be held at the [CVPR 2025](https://cvpr.thecvf.com/Conferences/2025) on June 11th, 2025 at the Music City Center, Nashville, TN, USA. Details will follow.

## Abstract

On-road testing of autonomous vehicles presents significant challenges in terms of cost and safety, underscoring the importance of simulation as a crucial tool to accelerate the development of safe autonomous driving (AD), a technology with enormous real-world impact. To extract useful information from simulation, minimizing the sim-to-real gap by developing good agent behavior models, and ensuring faithful perception simulation is essential. While recent years have witnessed a surge of publications in this rapidly evolving field, several fundamental questions remain unanswered, with the research often scattered across different robotics and machine learning venues and research fields. 

This workshop aims to unite leading researchers from various specializations, including perception simulation, behavior modeling, planner development, and safety research, to foster interdisciplinary conversations and collaboration.

## Call for Papers

### Important Dates 📅
- Paper Submission Opens: ~~February 18, 2025~~
- Paper Submission Deadline: ~~March 15, 2025~~
- Notification to Authors: ~~March 31, 2025~~
- Camera-Ready Submission: ~~April 7, 2025~~

### Submission Guidelines 🔔
We invite submissions of high-quality research to our **Archival** and **Non-Archival** tracks. All accepted papers will be eligible for poster presentation. A select number of papers will be chosen for spotlight presentations at the workshop. You need an openreview account for submission.

### Topics 🚘

We welcome contributions in the Autonomous Driving domain in the following areas (but not limited to):

- Improve fidelity and diversity of generative models for behavior and sensor simulation,
- Develop new metrics for the quality and coverage of generated scenarios,
- Combine behavior modeling, perception simulation, and safety requirements,
- Create trust and assess the credibility of the simulation toolchain, and
- Effectively use simulation to evaluate autonomous vehicles, 
- Effectively use simulation to train autonomous vehicles in closed loop,
- Incorporate recent advances from other fields, such as RL or foundation models.

For inquiries, feel free to reach out to the organizing committee at: [agents4ad@googlegroups.com](mailto:agents4ad@googlegroups.com)

## Agenda

<!-- script to display conference time -->
<script>
  var x = setInterval(function() {
    var d = new Date();
    var n = d.toLocaleTimeString("en-US", {timeZone: "America/Chicago", hour: '2-digit', minute:'2-digit', hour12: false})
    document.getElementById("centraltime").innerHTML = n
  }, 1000);
</script>

This full day workshop will take place on Wednesday June 11th, 08:30 to 17:50 CDT (UTC-5).

Below times are in Nashville time. Current time in Nashville is <span id="centraltime"></span>.

{% include schedule.liquid %}

## Invited Speakers

{% include feature_row.liquid id="schedule" %}

## Organizers

{% include feature_row.liquid id="organizers_row" %}

Contact: [agents4ad@googlegroups.com](mailto:agents4ad@googlegroups.com)

## Program Committee

The DDADS workshop organizers would like to extend our sincere gratitude to the community of reviewers who generously volunteered their time and expertise to evaluate submissions for our workshop. 
 
* Frieda Rong
* Ioan Andrei Bârsan
* Reinis Cimurs 
* Shu-Yuan Liu
* Thomas Roddick
* Vishal Kirankumar Shah 
* Zhejun Zhang
