"""
Test script to verify that the weather classification app is set up correctly
"""
import os
import sys

def check_files():
    """Check if all required files exist"""
    print("\n" + "="*60)
    print("CHECKING FILE STRUCTURE")
    print("="*60)
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        'static/css/style.css',
        'static/js/script.js'
    ]
    
    all_good = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_good = False
    
    # Check for model file (critical)
    model_exists = os.path.exists('best_model.h5')
    print(f"\n{'✓' if model_exists else '✗'} best_model.h5 (CRITICAL!)")
    
    if not model_exists:
        print("\n⚠️  WARNING: best_model.h5 NOT FOUND!")
        print("   You MUST copy your trained model here:")
        print("   From: C:\\Users\\admin\\Downloads\\Weather\\Weather3\\results\\best_model.h5")
        print("   To:   [This directory]\\best_model.h5")
        all_good = False
    
    return all_good and model_exists

def check_dependencies():
    """Check if required Python packages are installed"""
    print("\n" + "="*60)
    print("CHECKING PYTHON DEPENDENCIES")
    print("="*60)
    
    required_packages = {
        'flask': 'Flask',
        'tensorflow': 'TensorFlow',
        'numpy': 'NumPy',
        'PIL': 'Pillow',
        'sklearn': 'scikit-learn'
    }
    
    all_installed = True
    for module_name, package_name in required_packages.items():
        try:
            __import__(module_name)
            print(f"✓ {package_name}")
        except ImportError:
            print(f"✗ {package_name} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_python_version():
    """Check Python version"""
    print("\n" + "="*60)
    print("CHECKING PYTHON VERSION")
    print("="*60)
    
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✓ Python version is compatible")
        return True
    else:
        print("✗ Python 3.8 or higher required")
        return False

def main():
    """Run all checks"""
    print("\n" + "="*60)
    print("🌦️  WEATHER CLASSIFICATION APP - SETUP VERIFICATION")
    print("="*60)
    
    checks = {
        'Python Version': check_python_version(),
        'File Structure': check_files(),
        'Dependencies': check_dependencies()
    }
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    for check_name, passed in checks.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {check_name}")
    
    all_passed = all(checks.values())
    
    print("\n" + "="*60)
    if all_passed:
        print("✅ ALL CHECKS PASSED!")
        print("="*60)
        print("\nYou're ready to start the app!")
        print("\nRun: python app.py")
        print("Then open: http://localhost:5000")
    else:
        print("⚠️  SOME CHECKS FAILED")
        print("="*60)
        print("\nPlease fix the issues above before starting the app.")
        print("\nFor help, check:")
        print("  - README.md")
        print("  - QUICKSTART.md")
    
    print("\n")
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
