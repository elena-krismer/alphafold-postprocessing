from setuptools import setup, find_packages

setup(
    name='alphafold_postprocessing',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
       'setuptools',
       'matplotlib >= 3.8.0',
       'numpy >= 1.26.0',
       'jax==0.4.0',
       'jaxlib==0.4.0'
    ],
    entry_points={
        'console_scripts': [
            'alphafold_postprocessing=alphafold_postprocessing.cli:cli_main',
        ],
    },
    author='Gerhard Bräunlich, Simon Rüdisser',
    author_email='gerhard.braeunlich@id.ethz.ch, simon.ruedisser@biol.ethz.ch',
    description='alphafold2 postprocessing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/elena-krismer/alphafold-postprocessing',
    license='MIT',
)