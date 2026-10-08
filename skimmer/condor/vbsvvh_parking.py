"""
B-parking HH data (ParkingHH / ParkingHH0 / ParkingHH1), 2023-2026, for the
0Lep channels. Requested 2026-10-08; submitted in full at the requester's
explicit direction.

############################################################################
# WARNING -- THIS LIST DOUBLE-COUNTS REAL DATA IF GLOBBED WHOLESALE.
#
# The 59 datasets cover only 47 DISTINCT RUN SETS. Seven run ranges appear
# under several reprocessing campaigns, verified by querying the actual run
# numbers from DAS (not inferred from dataset names):
#   ParkingHH runs [367770..369694] (89 runs) -- 4 copies:
#       Run2023C-22Sep2023_v4-v1
#       Run2023C-NanoAODv15_v4-v1
#       Run2023C-PromptNanoAODv12_v4-v1
#       Run2023C-PromptReco-v4
#   ParkingHH runs [367661..367758] (15 runs) -- 3 copies:
#       Run2023C-22Sep2023_v3-v1
#       Run2023C-NanoAODv15_v3-v1
#       Run2023C-PromptNanoAODv12_v3-v1
#   ParkingHH runs [369869..370580] (50 runs) -- 3 copies:
#       Run2023D-22Sep2023_v1-v1
#       Run2023D-NanoAODv15-v1
#       Run2023D-PromptReco-v1
#   ParkingHH runs [370666..370790] (13 runs) -- 3 copies:
#       Run2023D-22Sep2023_v2-v1
#       Run2023D-NanoAODv15_v2-v1
#       Run2023D-PromptReco-v2
#   ParkingHH runs [379415..380238] (51 runs) -- 2 copies:
#       Run2024C-2024CDEReprocessing-v1
#       Run2024C-MINIv6NANOv15-v1
#   ParkingHH runs [380306..380947] (47 runs) -- 2 copies:
#       Run2024D-2024CDEReprocessing-v1
#       Run2024D-MINIv6NANOv15-v1
#   ParkingHH runs [380963..381594] (49 runs) -- 2 copies:
#       Run2024E-2024CDEReprocessing-v1
#       Run2024E-MINIv6NANOv15-v1
#
# Totals: 6,384,394,970 events across the 47 distinct run sets, versus
# 7,335,364,263 if all 59 are summed -- a 1.15x inflation overall, and 3-4x
# on the 2023C/D ranges specifically.
#
# A note on the naming, which is easy to misread: the _v3 / _v4 suffixes are
# DIFFERENT RUN RANGES and both are needed (2023C v3 = runs 367661-367758,
# v4 = 367770-369694). Only the CAMPAIGNS WITHIN a run range duplicate each
# other. 2024F-I and all of 2025/2026 have no duplication at all -- their
# PromptReco-v1/-v2 really are separate run ranges.
#
# Pick ONE campaign per duplicated run range downstream. For consistency with
# the rest of the v15 production that would be NanoAODv15* for 2023C/D and
# MINIv6NANOv15 for 2024C/D/E.
############################################################################
"""

from metis.Sample import DBSSample


nanoaodv15_run3_data_parking = [
    # ParkingHH Run2023C
    DBSSample(dataset="/ParkingHH/Run2023C-22Sep2023_v3-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023C-22Sep2023_v4-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023C-NanoAODv15_v3-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023C-NanoAODv15_v4-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023C-PromptNanoAODv12_v3-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023C-PromptNanoAODv12_v4-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023C-PromptReco-v4/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    # ParkingHH Run2023D
    DBSSample(dataset="/ParkingHH/Run2023D-22Sep2023_v1-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023D-22Sep2023_v2-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023D-NanoAODv15-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023D-NanoAODv15_v2-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023D-PromptReco-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2023D-PromptReco-v2/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    # ParkingHH Run2024A
    DBSSample(dataset="/ParkingHH/Run2024A-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024B
    DBSSample(dataset="/ParkingHH/Run2024B-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024C
    DBSSample(dataset="/ParkingHH/Run2024C-2024CDEReprocessing-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2024C-MINIv6NANOv15-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2024C-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024D
    DBSSample(dataset="/ParkingHH/Run2024D-2024CDEReprocessing-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2024D-MINIv6NANOv15-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2024D-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024E
    DBSSample(dataset="/ParkingHH/Run2024E-2024CDEReprocessing-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2024E-MINIv6NANOv15-v1/NANOAOD"),  # DUPLICATE RUN RANGE -- see header
    DBSSample(dataset="/ParkingHH/Run2024E-PromptReco-v1/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024E-PromptReco-v2/NANOAOD"),
    # ParkingHH Run2024F
    DBSSample(dataset="/ParkingHH/Run2024F-MINIv6NANOv15-v4/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024F-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024G
    DBSSample(dataset="/ParkingHH/Run2024G-MINIv6NANOv15-v3/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024G-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024H
    DBSSample(dataset="/ParkingHH/Run2024H-MINIv6NANOv15-v3/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024H-PromptReco-v1/NANOAOD"),
    # ParkingHH Run2024I
    DBSSample(dataset="/ParkingHH/Run2024I-MINIv6NANOv15-v3/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024I-PromptReco-v1/NANOAOD"),
    DBSSample(dataset="/ParkingHH/Run2024I-PromptReco-v2/NANOAOD"),
    # ParkingHH0 Run2025B
    DBSSample(dataset="/ParkingHH0/Run2025B-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2025C
    DBSSample(dataset="/ParkingHH0/Run2025C-PromptReco-v1/NANOAOD"),
    DBSSample(dataset="/ParkingHH0/Run2025C-PromptReco-v2/NANOAOD"),
    # ParkingHH0 Run2025D
    DBSSample(dataset="/ParkingHH0/Run2025D-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2025E
    DBSSample(dataset="/ParkingHH0/Run2025E-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2025F
    DBSSample(dataset="/ParkingHH0/Run2025F-PromptReco-v1/NANOAOD"),
    DBSSample(dataset="/ParkingHH0/Run2025F-PromptReco-v2/NANOAOD"),
    # ParkingHH0 Run2025G
    DBSSample(dataset="/ParkingHH0/Run2025G-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2026A
    DBSSample(dataset="/ParkingHH0/Run2026A-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2026B
    DBSSample(dataset="/ParkingHH0/Run2026B-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2026C
    DBSSample(dataset="/ParkingHH0/Run2026C-PromptReco-v1/NANOAOD"),
    # ParkingHH0 Run2026D
    DBSSample(dataset="/ParkingHH0/Run2026D-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2025B
    DBSSample(dataset="/ParkingHH1/Run2025B-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2025C
    DBSSample(dataset="/ParkingHH1/Run2025C-PromptReco-v1/NANOAOD"),
    DBSSample(dataset="/ParkingHH1/Run2025C-PromptReco-v2/NANOAOD"),
    # ParkingHH1 Run2025D
    DBSSample(dataset="/ParkingHH1/Run2025D-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2025E
    DBSSample(dataset="/ParkingHH1/Run2025E-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2025F
    DBSSample(dataset="/ParkingHH1/Run2025F-PromptReco-v1/NANOAOD"),
    DBSSample(dataset="/ParkingHH1/Run2025F-PromptReco-v2/NANOAOD"),
    # ParkingHH1 Run2025G
    DBSSample(dataset="/ParkingHH1/Run2025G-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2026A
    DBSSample(dataset="/ParkingHH1/Run2026A-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2026B
    DBSSample(dataset="/ParkingHH1/Run2026B-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2026C
    DBSSample(dataset="/ParkingHH1/Run2026C-PromptReco-v1/NANOAOD"),
    # ParkingHH1 Run2026D
    DBSSample(dataset="/ParkingHH1/Run2026D-PromptReco-v1/NANOAOD"),
]
