Summary:	Allows manipulation of cpusets on system and provides higher level functions
Name:		cpuset
Version:	1.5.5
Release:	%mkrel 1
License:	GPLv2
Group:		System/Kernel and hardware
URL:		http://code.google.com/p/cpuset
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cpuset is a Python application to make using the cpusets facilities in the
Linux kernel easier.  The actual included command is called cset and it allows
manipulation of cpusets on the system and provides higher level functions such
as implementation and control of a basic CPU shielding setup.

%prep

%setup -q

%build
CFLAGS="%{optflags}" \
%{__python} setup.py build
#make doc  ->not yet, asciidoc is missing...

%install
%{__rm} -rf %{buildroot}

# Install binaries, but do not install docs via setup.py
%{__python} setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-data=/eraseme
%{__rm} -rf %{buildroot}/eraseme

# Install documentation
%{__mkdir_p} %{buildroot}/%{_defaultdocdir}/cpuset
%{__cp} NEWS README INSTALL AUTHORS COPYING cset.init.d %{buildroot}/%{_defaultdocdir}/cpuset/
%{__mkdir_p} %{buildroot}/%{_mandir}/man1
cd doc
%{__cp} *.1 %{buildroot}/%{_mandir}/man1
%{__cp} *.txt %{buildroot}/%{_defaultdocdir}/cpuset/
%{__mkdir} %{buildroot}/%{_defaultdocdir}/cpuset/html
%{__cp} *.html %{buildroot}/%{_defaultdocdir}/cpuset/html/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cset
%{python_sitelib}/*
%{_mandir}/man1/*
%{_defaultdocdir}/*
