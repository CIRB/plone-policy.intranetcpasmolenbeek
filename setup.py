from setuptools import setup, find_packages

version = '1.0.2'

setup(name='policy.intranetcpasmolenbeek',
      version=version,
      description="Policy of intranet CPAS Molenbeek site",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          # -*- Extra requirements: -*-
          'collective.anysurfer',
          'collective.ckeditor',
          'collective.languagemovefolders',
          'collective.quickupload',
          'plone.app.ldap',
          'Products.PloneFormGen',
          'qi.portlet.TagClouds',
          'quintagroup.analytics',
          'webcouturier.dropdownmenu',
#          'plonetheme.intranetcpasmolenbeek',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
