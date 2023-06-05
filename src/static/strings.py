builds = """builds:
- name: approach_important
  tasks:
  - map_gray_centaurs
- name: audience_stand
  tasks:
  - enable_fuchsia_fairies
  - read_blue_witches
  - upgrade_olive_gnomes
- name: time_alone
  tasks:
  - design_olive_cyclops
  - upgrade_lime_leprechauns
"""

tasks = """tasks:
- name: bring_black_leprechauns
  dependencies: []
- name: bring_gray_cyclops
  dependencies: []
- name: bring_green_cyclops
  dependencies: []
- name: bring_purple_leprechauns
  dependencies: []
- name: bring_yellow_cyclops
  dependencies: []
- name: build_blue_leprechauns
  dependencies:
  - bring_purple_leprechauns
- name: build_lime_cyclops
  dependencies: []
- name: coloring_green_cyclops
  dependencies:
  - bring_gray_cyclops
  - enable_white_cyclops
  - read_lime_cyclops
- name: create_green_cyclops
  dependencies:
  - bring_green_cyclops
  - design_silver_cyclops
  - enable_yellow_cyclops
  - read_aqua_cyclops
  - train_white_cyclops
- name: create_white_cyclops
  dependencies: []
- name: design_black_centaurs
  dependencies: []
- name: design_olive_cyclops
  dependencies:
  - coloring_green_cyclops
  - create_green_cyclops
  - design_teal_cyclops
- name: design_silver_cyclops
  dependencies: []
- name: design_teal_cyclops
  dependencies:
  - bring_yellow_cyclops
  - build_lime_cyclops
  - create_white_cyclops
  - map_black_cyclops
- name: enable_fuchsia_fairies
  dependencies: []
- name: enable_white_cyclops
  dependencies: []
- name: enable_yellow_cyclops
  dependencies: []
- name: map_black_cyclops
  dependencies: []
- name: map_gray_centaurs
  dependencies:
  - read_purple_centaurs
  - train_silver_centaurs
- name: read_aqua_cyclops
  dependencies: []
- name: read_blue_witches
  dependencies: []
- name: read_lime_cyclops
  dependencies: []
- name: read_purple_centaurs
  dependencies: []
- name: train_silver_centaurs
  dependencies:
  - design_black_centaurs
  - upgrade_blue_centaurs
- name: train_white_cyclops
  dependencies: []
- name: upgrade_blue_centaurs
  dependencies: []
- name: upgrade_lime_leprechauns
  dependencies:
  - bring_black_leprechauns
  - build_blue_leprechauns
  - write_lime_leprechauns
- name: upgrade_olive_gnomes
  dependencies: []
- name: upgrade_olive_leprechauns
  dependencies: []
- name: write_aqua_leprechauns
  dependencies: []
- name: write_lime_leprechauns
  dependencies:
  - upgrade_olive_leprechauns
  - write_aqua_leprechauns
"""