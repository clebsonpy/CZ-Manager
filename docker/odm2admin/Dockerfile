FROM thinkwhere/gdal-python

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

LABEL description='Django admin app for Observation Data Model 2 (ODM2)' \
      url='https://github.com/miguelcleon/ODM2-Admin' \
      author='Miguel Leon' \
      author_email='leonmi@sas.upenn.edu' \
      development_status='5 - Production/Stable' \
      environment='Console' \
      intended_audience='Science/Research, Developers, Education' \
      license='MIT License' \
      operating_system='OS Independent' \
      programming_language='Python' \
      topic='Scientific/Engineering, Education'

RUN apt-get update --fix-missing && apt-get install --yes apt-utils postgresql-client

EXPOSE 8000

# && latest=$(git describe --tags) && git checkout ${latest}
RUN git clone "https://github.com/clebsonpy/CZ-Manager"
RUN cd CZ-Manager


WORKDIR /CZ-Manager

VOLUME templatesAndSettings/settings/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY docker/odm2admin/odm2database/odm2adminDB.sql /odm2adminDB.sql
COPY docker/odm2admin/odm2database/cvload.py /cvload.py

COPY docker/odm2admin/wait-for-postgres.sh /wait-for-postgres.sh
COPY docker/odm2admin/startup.sh /startup.sh

RUN chmod 755 /wait-for-postgres.sh
RUN chmod 755 /startup.sh

CMD ["/bin/bash", "/wait-for-postgres.sh", "/startup.sh"]
