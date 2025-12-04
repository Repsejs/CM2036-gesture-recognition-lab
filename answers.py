"""
Student Answer Sheet for Gesture Recognition Lab

Fill in your answers below for each step. Run this file to check your answers:
    uv run python answers.py

Your answers will be checked automatically, but the correct answers are not shown.
"""

# =============================================================================
# STEP 2: Load the Data
# =============================================================================

# 2.1: What separator character does the CSV use?
answer_2_1 = "YOUR_ANSWER_HERE"

# 2.2: What pandas method shows the first N rows?
answer_2_2 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 3: Explore and Clean the Data
# =============================================================================

# 3.1: What method finds unique values in a column?
answer_3_1 = "YOUR_ANSWER_HERE"

# 3.2: What method checks for missing values?
answer_3_2 = "YOUR_ANSWER_HERE"

# 3.3: What method counts occurrences of each value?
answer_3_3 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 4: Preprocess the Data
# =============================================================================

# 4.1: What method removes rows with missing values?
answer_4_1 = "YOUR_ANSWER_HERE"

# 4.2: What operator performs integer division in Python?
answer_4_2 = "YOUR_ANSWER_HERE"

# 4.3: What method reshapes a numpy array?
answer_4_3 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 6: Encode Labels
# =============================================================================

# 6.1: What sklearn class converts text labels to numbers?
answer_6_1 = "YOUR_ANSWER_HERE"

# 6.2: What method both fits and transforms in one call?
answer_6_2 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 7: Normalize the Data
# =============================================================================

# 7.1: What sklearn class performs standardization?
answer_7_1 = "YOUR_ANSWER_HERE"

# 7.2: What does -1 mean in reshape(-1)?
# Options: "flatten all dimensions", "infer this dimension", "reverse dimension"
answer_7_2 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 8: Data Augmentation
# =============================================================================

# 8.1: What slicing syntax reverses the middle dimension of a 3D array?
# Hint: array[:, ???, :]
answer_8_1 = "YOUR_ANSWER_HERE"

# 8.2: What numpy function stacks arrays vertically?
answer_8_2 = "YOUR_ANSWER_HERE"

# 8.3: What numpy function concatenates arrays?
answer_8_3 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 10: Split the Data
# =============================================================================

# 10.1: What function splits data into train/test sets?
answer_10_1 = "YOUR_ANSWER_HERE"

# 10.2: For an 80/20 split, what value should test_size be?
answer_10_2 = "YOUR_ANSWER_HERE"

# 10.3: What parameter ensures balanced class distribution in both sets?
answer_10_3 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 11: Build the Neural Network
# =============================================================================

# 11.1: What layer converts 3D input to 1D (flattens it)?
answer_11_1 = "YOUR_ANSWER_HERE"

# 11.2: What activation function is commonly used in hidden layers?
# Options: "relu", "sigmoid", "tanh", "linear"
answer_11_2 = "YOUR_ANSWER_HERE"

# 11.3: What activation function should be used for multi-class classification output?
# Options: "relu", "sigmoid", "softmax", "tanh"
answer_11_3 = "YOUR_ANSWER_HERE"

# 11.4: What does the Dropout layer do?
# Options: "removes features", "prevents overfitting", "speeds training", "normalizes"
answer_11_4 = "YOUR_ANSWER_HERE"

# 11.5: In the Dense layer, what parameter determines how many neurons it has?
# Hint: It's the first parameter, like Dense(128, ...)
answer_11_5 = "YOUR_ANSWER_HERE"


# =============================================================================
# STEP 12: Compile the Model
# =============================================================================

# 12.1: What optimizer is used in this lab?
answer_12_1 = "YOUR_ANSWER_HERE"

# 12.2: What loss function is used for multi-class classification with integer labels?
answer_12_2 = "YOUR_ANSWER_HERE"


# =============================================================================
# CONCEPTUAL QUESTIONS
# =============================================================================

# Q1: Why do we normalize data before training? (one word)
# Options: "speed", "scale", "accuracy", "memory"
conceptual_1 = "YOUR_ANSWER_HERE"

# Q2: Why do we split data into train and test sets? (choose one)
# Options: "generalization", "speed", "memory", "visualization"
conceptual_2 = "YOUR_ANSWER_HERE"

# Q3: What does the time reversal augmentation technique assume?
# Options: "reversible", "symmetric", "periodic", "random"
conceptual_3 = "YOUR_ANSWER_HERE"


# =============================================================================
# DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def check_answers():
    """Check student answers without revealing solutions."""
    import hashlib

    def hash_answer(answer):
        """Create hash of answer for comparison."""
        return hashlib.sha256(str(answer).lower().strip().encode()).hexdigest()

    # Correct answer hashes (students cannot reverse these)
    correct_hashes = {
        'answer_2_1': '41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4',
        'answer_2_2': '9f2e6d33a3717ee826353a404ba4618d1aeeb6879ad7936bce8ed5f46814924d',
        'answer_3_1': 'c2720445a45267813688ff73fa188aa060c1b661aefaf1650d42f690697b5ab3',
        'answer_3_2': '5e840ddef2e5589d8402424eb76c5161b62526feaf74962c1c04d9e65fe2ce60',
        'answer_3_3': '0abf75cb8d662b3829b7f2d9aa8f34e2ea89ccf0e03cb19da9c958b24a9541a7',
        'answer_4_1': 'efb170244f0caeba3c56e4cd069b256eb16897e3d580ff391aa61ce243422612',
        'answer_4_2': 'a2c2339691fc48fbd14fb307292dff3e21222712d9240810742d7df0c6d74dfb',
        'answer_4_3': 'ddf782b99e895d8b2d8b47cccac9098a10ec11e287b51548c0811aaccf1473f6',
        'answer_6_1': '0e941b1306bb037f5822a59fef20b98b378ebdcd503c8592eed8764b399739dc',
        'answer_6_2': '6b7c4d431b2c929fc4ea4c2ae75f7d1cbdfc2b413e477f9c0ce56b4a80998753',
        'answer_7_1': 'baa8890451bab28ebcc856fdf40c543c0d85476bc258cbf453bce1462a35e991',
        'answer_7_2': '472ae70b4ff54a9184fefd5142f02014f6467406b0893c61fd2113dc518e23f9',
        'answer_8_1': '63b6bbe5568b83890c16d1184ae77cf6e821b52e8a3ef446e307e72209699de3',
        'answer_8_2': '1af596367e029fb4958ecca19ef636bbe2938a59763e255a9d9002a52634823d',
        'answer_8_3': '0afe756cd1e815034cfaf42660ea13c6eec402a3b9c4359838ed90dfb89ad2c3',
        'answer_10_1': '0c5cb36827a5f7ca4b84772c1af3e6ff84b83e986c6d0b9dd71d7ce2da84da1d',
        'answer_10_2': '44896b09365746b5f7167ee4d64988a38f7f4628803cbf86224e74eeb7c69e9d',
        'answer_10_3': '58c512f150039c897f3100160a7099bb188d45e2a7dddce9a31406100c0dc93f',
        'answer_11_1': '3ab675f2b94ec6889fc354439d5f31c7278f7a7ef414645c774017e1bdac24dc',
        'answer_11_2': '99e2995dbca8ca48ab1e5e0b7946ea783a9f242fb8ea1482dd8c8aca7e2805b8',
        'answer_11_3': '9a5fd614ff183bba6984eec7fc8f987da2a165a07af70e2f885277055925f534',
        'answer_11_4': '3e6eda4f4c4c1f4ca7f12283729a197717a7b364e6c8cf63cad8c4f84d3e3dd8',
        'answer_11_5': 'c981a30c0e7b420b0ba50ce7d1d4174a511fdf20567b852ab02c774cb9a3591e',
        'answer_12_1': 'f7f376a1fcd0d0e11a10ed1b6577c99784d3a6bbe669b1d13fae43eb64634f6e',
        'answer_12_2': 'd4dd992c24b0136dbebc57a3f1a42893fe77463d559f388ee1f1ef5f7c6b5605',
        'conceptual_1': 'f469802a31447f90d6a033d43f18db7ebfbee7cc3c378024bcc0f1573d3feef8',
        'conceptual_2': '23d5e1e004ec63f2d78179d7fe643843e6f406b13af38eaeb252cebb5236d555',
        'conceptual_3': '31a2b0e3d089e3179fc12083834f721561357e6c0c2d05d580fb188e4c753a00',
    }

    # Get all answer variables from globals
    answers = {k: v for k, v in globals().items() if k.startswith('answer_') or k.startswith('conceptual_')}

    # Define the correct display order (by step number, then conceptual)
    answer_order = [
        # Step 2
        'answer_2_1', 'answer_2_2',
        # Step 3
        'answer_3_1', 'answer_3_2', 'answer_3_3',
        # Step 4
        'answer_4_1', 'answer_4_2', 'answer_4_3',
        # Step 6
        'answer_6_1', 'answer_6_2',
        # Step 7
        'answer_7_1', 'answer_7_2',
        # Step 8
        'answer_8_1', 'answer_8_2', 'answer_8_3',
        # Step 10
        'answer_10_1', 'answer_10_2', 'answer_10_3',
        # Step 11
        'answer_11_1', 'answer_11_2', 'answer_11_3', 'answer_11_4', 'answer_11_5',
        # Step 12
        'answer_12_1', 'answer_12_2',
        # Conceptual
        'conceptual_1', 'conceptual_2', 'conceptual_3',
    ]

    total = 0
    correct = 0
    results = []

    for var_name in answer_order:
        if var_name not in answers:
            continue
        student_answer = answers[var_name]
        if student_answer == "YOUR_ANSWER_HERE":
            results.append(f"⊘ {var_name}: Not answered yet")
            total += 1
        else:
            total += 1
            student_hash = hash_answer(student_answer)
            if var_name in correct_hashes and student_hash == correct_hashes[var_name]:
                results.append(f"✓ {var_name}: Correct!")
                correct += 1
            else:
                results.append(f"✗ {var_name}: Incorrect (try again)")

    print("\n" + "="*70)
    print("ANSWER VERIFICATION RESULTS")
    print("="*70)
    for result in results:
        print(result)

    print("\n" + "="*70)
    print(f"Score: {correct}/{total} ({100*correct//total if total > 0 else 0}%)")
    print("="*70)

    if correct == total:
        print("\n🎉 Perfect score! You've answered all questions correctly!")
    elif correct >= total * 0.8:
        print("\n👍 Great job! Review the incorrect answers and try again.")
    elif correct >= total * 0.5:
        print("\n📚 Good effort! Keep reviewing the concepts and trying.")
    else:
        print("\n💪 Keep learning! Review the notebook and try again.")
    print()

if __name__ == "__main__":
    check_answers()
