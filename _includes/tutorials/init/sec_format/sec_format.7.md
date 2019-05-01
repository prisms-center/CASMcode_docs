The only input file not described via `` `casm format` `` is the `` `casm learn` `` input file used to specify options controlling fitting expansion coefficients. A description of this file can be printed with `` `casm learn --settings-format` ``:

```
$ casm learn --settings-format
```
<details><summary markdown="span">See result</summary>

```
$ casm learn --settings-format

  Settings file description:
  ------------------------------------------------------------------------------
  {

  # The "problem_specs" options specify which data to use and how to score
  # candidate solutions. It consists primarily of "data", "weight", and "cv"
  # settings.

    "problem_specs" : {

  # The "problem_specs"/"data" options specify the data to use for learning
  #
  #   A filename and filetype describing where to find data to use for learning.
  #   Also includes the labels of the sample ('X') and target ('y') data to use
  #   and kwargs containing additional options.
  #
  #
  # Object attributes
  # -----------------
  #
  # filename: string, optional, default="train"
  #   The path to a file containing the training data
  #
  # filetype: string, optional, default="selection"
  #   Options:
  #     "selection": path to a CASM selection file. Only the selected
  #        configurations included in the file will be used for training. The
  #        data, typically correlations and a property, can be queried separately
  #        and do not need to be included. If they do exist, the data in the file
  #        will be used.
  #     "csv": path to a CSV file
  #     "json": path to a JSON file
  #
  # X: string, optional, default="corr"
  #   The name of sample data. Expected to take the form "X(0)", "X(1)", etc...
  #
  # y: string, optional, default="formation_energy"
  #   The name of the target value to train with.
  #
  # kwargs: dict or null, optional, default=dict()
  #   Additional parameters to be used to get training data.
  #
  #   Options for 'filetype' "selection":
  #     "project_path": indicate the path to a CASM project. Default null uses
  #       the CASM project containing the current working directory. This option
  #       is not currently implemented, but included as a placeholder. Currently
  #       'casm-learn' must be run from inside a CASM project.
  #
  #   Options for 'filetype' "csv":
  #     Any options to pass to pandas.read_csv
  #
  #   Options for 'filetype' "json":
  #     Any options to pass to pandas.read_json

      "data" : {
        "filename": "train",
        "filetype": "selection",
        "X": "corr",
        "y": "formation_energy",
        "kwargs": null
      },

  # The "problem_specs"/"weight" options specify the method to use for weighting
  # training data.
  #
  #   Ordinary least squares minimizes
  #     (y-X*b).transpose() * (y-X*b)
  #
  #   where 'X' is the correlation matrix of shape (Nvalue, Nbfunc), and 'y'
  #   is a vector of Nvalue calculated properties, and 'b' are the fitting
  #   coefficients (ECI).
  #
  #   Weighted least squares minimizes
  #     (y-X*b).transpose() * W * (y-X*b)
  #
  #   Using the SVD, and given that W is Hermitian:
  #     U * S * U.transpose() == W
  #
  #   Define L such that:
  #     L.transpose() = U * sqrt(S)
  #
  #   Then we can write the weighted least squares problem using:
  #     (y-X*b).transpose() * L.transpose() * L * (y-X*b)
  #
  #   Or:
  #     (L*y-L*X*b).transpose() * (L*y-L*X*b)
  #
  #   So, if weights are included, then the linear model is changed from
  #     X*b = y  ->  L*X*b = L*y
  #
  #   By default, W = np.matlib.eye(Nvalue) (unweighted).
  #
  #   If the weighting method provides 1-dimensional input (this is typical), in
  #   a numpy array called 'w':
  #     W = np.diag(w)*Nvalue/np.sum(w)
  #
  #   If the 'custom2d' method is used, the input W_in must by Hermitian,
  #   positive-definite and is normalized by:
  #     W = W_in*Nvalue/np.sum(W_in)
  #
  #
  # Object attributes
  # -----------------
  #
  # method: string, optional, default=null
  #   The weighting method to use
  #
  #   Options:
  #   'wHullDist': Weight according to w_i = A*exp(-hull_dist/kT) + B, where A, B,
  #     and kT are user-defined kwargs parameters, and hull_dist is the distance
  #     from the convex hull of the training data, using the kwarg "hull_selection"
  #     to determine which selection of configurations to use to find the hull.
  #     The default hull_selection is "CALCULATED".
  #   'wEmin': Weight according to w_i = A*exp(-dist_from_minE/kT) + B,
  #     where A, B, and kT are user-defined kwargs parameters, and dist_from_minE
  #     is calculated from the training data
  #   'wEref': weight according to w_i = A*exp(-(formation_energy - E0)/kT) + B, for
  #     (formation_energy - E0) > 0.0; and w_i = 1.0 if (formation_energy - E0) <= 0.0.
  #     where A, B, E0, and kT are user-defined kwargs parameters.
  #   'wCustom': Weights are read from a column titled 'weight' in the training data
  #     selection file.
  #   'wCustom2d': Weights are read from columns in the training data selection file,
  #     which are expected to be titled 'weight(0)' ... 'weight(Nvalue-1)'
  #
  #
  # kwargs: dict or null, optional, default=dict()
  #   Additional parameters to be used to construct the estimator
  #
  #   Options: (as described above)
  #     "A": float
  #     "B": float
  #     "kT": float
  #     "E0": float
  #     "hull_selection": string

      "weight": {
        "method": null,
        "kwargs": null
      },

  # The "problem_specs"/"cv" options specify how to generate cross validation sets.
  #
  #   The cv score reported is:
  #
  #     cv = sqrt(np.mean(scores)) + (Number of non-zero ECI)*penalty,
  #
  #   where 'scores' is an array containing the mean squared error calculated for
  #   each training/testing set, '(Number of non-zero ECI)' is the number of basis
  #   functions with non-zero ECI, and 'penalty' is the user-input penalty per basis
  #   function (default=0.0).
  #
  #
  # Object attributes
  # -----------------
  #
  # method: string
  #   A scikit-learn or casm cross validation method.
  #
  #   Options include 'KFold', 'ShuffleSplit', 'LeaveOneOut', etc.
  #     See: http://scikit-learn.org/stable/modules/model_selection.html
  #
  #   CASM also provides the following method:
  #    'cvCustom': Read a scikit-learn type 'cv' generator or training/test sets
  #       from a pickle file. This can be used to load the 'cv' data written by
  #       'casm-learn --checkspecs' by using the required kwarg 'filename'.
  #
  #     Note: The 'LinearRegression' estimator is implemented using
  #     casm.learn.linear_model.LinearRegressionForLOOCV', which solves X*b=y using:
  #       S = np.linalg.pinv(X.transpose().dot(X)).dot(X.transpose())
  #       b = np.dot(S, y)
  #       H = np.dot(X, S)
  #       y_pred = np.dot(H, y)
  #
  #     Note: When the estimator is 'LinearRegression', the 'LeaveOneOut'
  #     cross-validation score is calculated via:
  #
  #       LOOCV = np.mean(((y - y_pred)/(1.0 - np.diag(H)))**2)
  #
  # kwargs: dict or null, optional, default=dict()
  #   Additional parameters to be used to construct the cross-validation method
  #   constructor.
  #
  # penalty: float, optional, default=0.0
  #   The CV score is increased by 'penalty*(number of selected basis function)'

      "cv": {
        "method": "KFold",
        "kwargs": {
          "n_splits": 10,
          "shuffle": true
        },
        "penalty": 0.0
      },

  # The "problem_specs"/"specs_filename" option:
  #
  # Optional. Name to use for file storing the training data and CV train/test
  # sets. The default is determined from the input filename, for example,
  # 'my_input_specs.pkl' is used if the input file is named 'my_input.json'.

      "specs_filename": "problem_specs.pkl"

    },

  # The "estimator" option specifies a linear model estimator.
  #
  # Object attributes
  # -----------------
  #
  # method: string
  #   A scikit-learn linear model estimator.
  #
  #   Options: 'LinearRegression', 'Ridge', 'Lasso', 'LassoCV', etc.
  #     See: http://scikit-learn.org/stable/modules/linear_model.html
  #
  #   Note: The 'LinearRegression' estimator is implemented using
  #   casm.learn.linear_model.LinearRegressionForLOOCV', which solves X*b=y using:
  #     b = np.dot(S, y)
  #     S = np.linalg.pinv(X.transpose().dot(X)).dot(X.transpose())
  #     y_pred = np.dot(H, y)
  #     H = np.dot(X, S)
  #
  # kwargs: dict or null, optional, default=dict()
  #   Additional parameters to be used to construct the estimator
  #
  #   Options for "LinearRegression":
  #     "pinv": bool, optional, default=True
  #       If True, use the pseudo-inverse via np.linalg.pinv; else use np.linalg.inv.
  #
  #   Options for other methods:
  #     Any options to pass to the estimator construtor.
  #
  #   By default, the kwarg "fit_intercept" is set to False.

    "estimator": {
      "method": "LinearRegression",
      "kwargs": null
    },


  # The "feature_selection" option specifies a feature selection method.
  #
  # Object attributes
  # -----------------
  #
  # method: string
  #   A scikit-learn or casm.learn.feature_selection feature selection method.
  #
  #   Options from sklearn.feature_selection: "SelectFromModel", "RFE", etc.
  #     See: http://scikit-learn.org/stable/modules/feature_selection.html
  #
  #   Options from casm.learn.feature_selection:
  #
  #   "DirectSelection": Allows directly specifying which basis functions should
  #     be included.
  #
  #     Options for "kwargs":
  #
  #       "population": List[dict]
  #          Contains a list of options specifying which individuals to fit.
  #          Options are:
  #
  #            "bitstring": Ex.: {"bitstring" : "01110001100"}
  #              String consisting of '0' and '1', with '1' corresponding to
  #              selected basis functions. May be shorter than the total number
  #              of possible basis functions, in which case '0' are effectively
  #              padded to the end.
  #
  #            "indices": Ex.: {"indices" : [1, 2, 3, 7, 8]}
  #              List of indices of basis functions to be selected.
  #
  #            "from_halloffame": Ex.: { "from_halloffame" : "my_halloffame.pkl",
  #                                      "individuals" : [0, 2, 5]}
  #               Specifies a hall of fame .pkl file and particular individuals
  #               in the hall (by index) to include in the population. The
  #               "individuals" list is optional, with the default behaviour
  #               including all individuals in the hall of fame.
  #
  #       "use_saved_estimator": boolean, optional, default=False
  #          If True, and individuals in the input population come from a HallOfFame
  #          the estimator method stored in the individual's saved input file will
  #          be used instead of the estimator specified in the current input file.
  #
  #
  #   Evolutionary algorithms, from casm.learn.feature_selection, are implemented
  #   using deap: http://deap.readthedocs.org/en/master/index.html
  #
  #   "GeneticAlgorithm": Implements deap.algorithms.eaSimple, using selTournament,
  #     for selection, cxUniform for mating, and mutFlipBit for mutation. The
  #     probability of mating and mutating is set to 1.0.
  #
  #     Options for "kwargs":
  #
  #       "selTournamentSize": int, optional, default=3
  #          Tournament size. A larger tournament size weeds out less fit
  #          individuals more quickly, while a smaller tournament size weeds out
  #          less fit individuals more gradually.
  #
  #       "cxUniformProb": float, optional, default=0.5
  #          Probability of swapping bits during mating.
  #
  #       "mutFlipBitProb": float, optional, default=0.01
  #          Probability of mutating bits
  #
  #       "constraints_kwargs": dict, optional, default=dict()
  #          Keyword arguments for setting constraints on allowed individuals.
  #          See below for options.
  #
  #       "evolve_params_kwargs": dict, optional, default=dict()
  #          Keyword arguments for controlling how long the algorithm runs, how
  #          new random individuals are initialized, when restart files are
  #          written, and the names of the files. See below for options.
  #
  #
  #   "IndividualBestFirst":
  #     Implements a best first search optimization for each individual in the initial
  #     population. Each individual in the population is minimized by repeatedly begin
  #     replaced by its most fit child.
  #
  #     Children are generated by generating all the individual that differ from
  #     the parent by +/- 1 selected feature.
  #
  #
  #     Options for "kwargs":
  #
  #       "constraints_kwargs": dict, optional, default=dict()
  #          Keyword arguments for setting constraints on allowed individuals.
  #          See below for options.
  #
  #       "evolve_params_kwargs": dict, optional, default=dict()
  #          Keyword arguments for controlling how long the algorithm runs, how
  #          new random individuals are initialized, when restart files are
  #          written, and the names of the files. See below for options.
  #
  #
  #   "PopulationBestFirst":
  #     Implements a best first search optimization for a population of individual
  #     solutions. Each individual is associated with a 'status' that indicates
  #     whether it has had children yet or not. At each step, the most fit individual
  #     that hasn't had children has children and the population is updated to keep
  #     only the 'n_population' most fit individuals. The algorithm stops when all
  #     individuals in the population have had children.
  #
  #     Children are generated by generating all the individual that differ from
  #     the parent by +/- 1 selected feature.
  #
  #     Options for "kwargs":
  #
  #       "constraints_kwargs": dict, optional, default=dict()
  #          Keyword arguments for setting constraints on allowed individuals.
  #          See below for options.
  #
  #       "evolve_params_kwargs": dict, optional, default=dict()
  #          Keyword arguments for controlling how long the algorithm runs, how
  #          new random individuals are initialized, when restart files are
  #          written, and the names of the files. See below for options.
  #
  #
  #   The evolutionary algorithms have an optional set of "constraints_kwargs"
  #   parameters that may restrict the number of basis functions selected to some
  #    range, or enforce some basis functions to have or not have coefficients:
  #
  #   Options for "constraints_kwargs":
  #     "n_features_min": int, optional, default=1
  #        The minimum allowed number of selected features. Must be >=1.
  #
  #     "n_features_max": int or str, optional, default="all"
  #        The maximum allowed number of selected features. String "all" for no limit.
  #
  #     "fix_on": 1d array-like of int, optional, default=[]
  #        The indices of features to fix on
  #
  #     "fix_off": 1d array-like of int, optional, default=[]
  #        The indices of features to fix off
  #
  #
  #   The evolutionary algorithms share an optional set of "evolve_params_kwargs"
  #   parameters that control how long the algorithm runs, how new random
  #   individuals are initialized, when restart files are written, and the names
  #   of the files:
  #
  #   Options for "evolve_params_kwargs":
  #
  #     "n_population": int, optional, default=100
  #        Initial population size. This many random initial starting individuals
  #         are created if no "pop_begin_filename" file exists.
  #
  #     "n_halloffame": int, optional, default=25
  #        Maxsize of the hall of fame which holds the best individuals
  #        encountered in any generation. Upon completion, the individuals in
  #        this hall of fame are into your overall casm-learn hall of fame to
  #        be compared to results obtained from other fitting or feature
  #        selection methods.
  #
  #     "n_generation": int, optional, default=10
  #        Number of generations between saving the hall of fame.
  #
  #     "n_repetition": int, optional, default=100
  #        Number of repetitions of n_generation generations. Each repetition
  #        begins with the existing final population.
  #
  #     "n_features_init: int or "all", optional, default=0
  #        Number of randomly selected features to initialize each individual
  #        with.
  #
  #     "pop_begin_filename": string, optional, default="population_begin.pkl"
  #        Filename suffix where the initial population is read from, if it
  #        exists. For example, if "filename_prefix" is "Ef_kfold10" and
  #        "pop_begin_filename" is "population_begin.pkl", then the initial
  #        population is read from the file "Ef_kfold10_population_begin.pkl".
  #
  #        The population file may contain either a  list of individual,
  #        as written to the "population_end.pkl" file, or a HallOfFame
  #        instance, as written to either an "evolve_halloffame.pkl" file or
  #        overall casm-learn "halloffame.pkl" file.
  #
  #     "pop_end_filename": string, optional, default="population_end.pkl"
  #        Filename where the final population is saved. For example, if
  #        "filename_prefix" is "Ef_kfold10" and "pop_end_filename" is
  #        "population_end.pkl", then the final population is saved to the
  #        file "Ef_kfold10_population_end.pkl".
  #
  #     "halloffame_filename": string, optional, default="evolve_halloffame.pkl"
  #        Filename where a hall of fame is saved holding the best individuals
  #        encountered in any generation. For example, if "filename_prefix" is
  #        "Ef_kfold10" and "halloffame_filename" is "evolve_halloffame.pkl",
  #        then it is saved to the file "Ef_kfold10_evolve_halloffame.pkl".
  #
  #     "filename_prefix": string, optional
  #        Prefix for filenames, default uses input file filename excluding
  #        extension. For example, if input file is named "Ef_kfold10.json", then
  #        "Ef_kfold10_population_begin.pkl", "Ef_kfold10_population_end.pkl", and
  #        "Ef_kfold10_evolve_halloffame.pkl" are used.

    "feature_selection" : {
      "method": "GeneticAlgorithm",
      "kwargs": {
        "selTournamentSize": 3,
        "cxUniformProb": 0.5,
        "mutFlipBitProb": 0.01,
        "constraints": {
          "n_features_min": 1,
          "n_features_max": "all",
          "fix_on": [],
          "fix_off": []
        },
        "evolve_params_kwargs": {
          "n_population": 100,
          "n_generation": 10,
          "n_repetition": 100,
          "n_features_init": 0
        }
      }
    },

  # The "halloffame_filename" option:
  #
  # Optional. Default = "halloffame.pkl"
  # Name to use for file storing the best results obtained to date, as determined
  # by the CV score. This enables comparison of the results of various estimator
  # or feature selection methods.

      "halloffame_filename": "halloffame.pkl"

    },

  # The "n_halloffame" option:
  #
  # Optional. Default = 25
  # The number of individuals to store in the hall of fame.

    "n_halloffame": 25

  # The "checkspecs" option:
  #
  #   Currently, these settings are used with the '--checkspecs' option to control
  #   the output files containing training data (including calculated weights) and
  #   cv generators or training / testing sets.
  #
  #
  # Object attributes
  # -----------------
  #
  # data_filename: string
  #   The path to the file where the training data (including weights) should be
  #   written
  #
  # data_kwargs: dict or null, optional, default=dict()
  #   Additional parameters to be used to write training data.
  #
  #   Options for input 'filetype' "selection":
  #     None.
  #
  #   Options for input 'filetype' "csv":
  #     Any options to pass to pandas.to_csv
  #
  #   Options for input 'filetype' "json":
  #     Any options to pass to pandas.to_json
  #
  # cv_filename: string
  #   The path to the file where the cv generator or train/tests sets should be
  #   written as pickle file
  #
  # cv_kwargs: dict or null, optional, default=dict()
  #   Additional parameters to be used to write cv data using pickle.dump.

    "checkspecs" : {
      "data_filename": "check_train",
      "data_kwargs": null,
      "cv_filename": "check_cv.pkl",
      "cv_kwargs": null
    },

  # The "checkhull" option:
  #
  #   Currently, these settings are used with the '--checkhull' option to
  #   calculate convex hull properties.
  #
  #
  # Object attributes
  # -----------------
  #
  # selection: str, optional, default="ALL"
  #   A CASM selection (either 'casm select' output filename or one of the
  #   standard selections: "MASTER", "CALCULATED", or "ALL") containing all the
  #   configurations to be considered. The DFT convex hull is generated from
  #   the subset of this selection for which 'is_calculated' is true.
  #
  # write_results: bool, optional, default=False
  #   If True, write CASM selection files containing the output data. Output
  #   selection files are named "checkhull_(problem_specs_prefix)_(i)_(selname)",
  #   where 'problem_specs_prefix' is input["problem_specs_prefix"], 'i' is the
  #   index of the individual in the hall of fame, and 'selname' is one of:
  #     "dft_gs" : DFT calculated ground states
  #     "clex_gs" : predicted ground states
  #     "gs_missing" : DFT ground states that are not predicted ground states
  #     "gs_spurious" : Predicted ground states that are not DFT ground states
  #     "uncalculated" : Predicted ground states and near ground states that have not been calculated
  #     "below_hull" : All configurations predicted below the prediction of the DFT hull
  #
  # primitive_only: bool, optional, default=True
  #   If True, only use primitive configurations to construct the convex hull,
  #   else use all selected configurations.
  #
  # uncalculated_range: number, optional, default=0.0
  #   Include all configurations with clex_hull_dist less than this value (+hull_tol)
  #   in the "uncalculated" configurations results. Default only includes predicted
  #   ground states.
  #
  # ranged_rms: List[number], optional, default=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
  #   Calculates the root-mean-square error for DFT calculated configurations
  #   within a particular range (in eV/unitcell) of the DFT hull. The list
  #   provides all the ranges for which the RMSE is requested.
  #
  # composition: str, optional, default="atom_frac"
  #   Composition argument use for 'casm query' properties 'hull_dist' and
  #   'clex_hull_dist'. For thermodynamic ground states, use "atom_frac".
  #
  # hull_tol: number, optional, default=proj.settings.data["lin_alg_tol"]
  #   Tolerance used for identify hull states
  #
  # dim_tol: number, optional, default=1e-8
  #   Tolerance for detecting composition dimensionality
  #
  # bottom_tol: number, optional, default=1e-8
  #   Tolerance for detecting which facets form the convex hull bottom

    "checkhull" : {
      "selection": "ALL",
      "write_results": true,
      "primitive_only": true,
      "uncalculated_range": 1e-8,
      "ranged_rms": [0.001, 0.005, 0.01, 0.05, 0.1, 0.5],
      "composition": "atom_frac",
      "hull_tol": 1e-8,
      "dim_tol": 1e-8,
      "bottom_tol": 1e-8
    }

  }
  ------------------------------------------------------------------------------
```
</details>
<br>
