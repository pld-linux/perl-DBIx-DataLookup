#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	DataLookup
Summary:	DataLookup - Perl extension for database view lookup table.
#Summary(pl):	
Name:		perl-DBIx-DataLookup
Version:	0.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remotely similar to DBIx::Cache but is very simpler and serves narrower
purpose.  This module allows you to both cache records pulled by an SQL
statement from a database in the memory as well as look them up later
at any time during execution of your script.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}/%{pnam}

%build
perl -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"DBIx::DataLookup")'
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
