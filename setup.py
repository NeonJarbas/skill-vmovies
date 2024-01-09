#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-vmovies.jarbasai=skill_vmovies:VMoviesSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-vmovies',
    version='0.0.1',
    description='ovos V Movies skill plugin',
    url='https://github.com/JarbasSkills/skill-vmovies',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_vmovies": ""},
    package_data={'skill_vmovies': ['locale/*', 'res/*']},
    packages=['skill_vmovies'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
