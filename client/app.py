from flask import Flask, request, jsonify, render_template

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler